
- Start Date: 2024-07-10
- Target Major Version:
- Reference Issues: n/a
- Issue:
- Implementation PR: (leave this empty)


## Overview

The submission of a registration application currently creates an actual registration.

A registration should be created only once an application is approved either by auto approval or manual approval process.

## Motivation
To separate a registration application from an actual registration.

The application will go through various stages such as DRAFT, SUBMITTED, PAID, IN_REVIEW, APPROVED, REJECTED etc. till it gets converted to a registration.

Any future application like a renewal application will be stored in the same application table. This will enable the user to see the list of applications and actual registrations separately. For example, A renewal application
may make changes to the existing registration. But the user will be able to see both registration and renewal applications
under application history.

It is important to store the copy of user input without any alteration for any reference in the future. Moving to the application model will enable us to store the submission JSON as it is.



## Data Model

[Data Model](Data%20Model.jpg)


## Submission Flow
[Diagram](Application%20Submission%20Flow.jpg)
1. When an application is submitted, the application data will be stored in the applications table. The state of the application will be DRAFT by default.
2. STRR API will create an invoice in the SBC Pay.
3. Once the API receives invoice creation success message, the application state will be updated to SUBMITTED and success response will be returned to the UI.
4. Once the UI receives application submission success message, it will redirect to SBC Pay UI (Current behavior)
5. Once the payment is successful, the client UI will call update payment endpoint to update the application status to PAID. It will also update payment related information such as payment completion date.After successful update, success response will be returned to the UI.\
**Note:** The use of a event listener to listen to the payment events from SBC-PAY is recommended here because if the redirection fails for any reason/network error the update call will never happen and the application will be stuck in SUBMITTED state.
6. UI will show the submission confirmation to the user.

## Approval Flow
### Auto Approval Job
[Diagram](Auto%20Approval%20Process.jpg)
- Runs every hour or at predefined intervals.
- Fetches the PAID applications from the applications table.
- Runs the auto approval logic on the application and updated the application status to APPROVED, REVIEW_REQUIRED or PROVISIONAL. 
- If there is an error in the third party API call, the application will be marked for full review.
- If the application is approved, create the new registration in the registration + related tables. Create the auto approval record against the application.

### Full Review
- The staff can view the applications that are in the REVIEW_REQUIRED, IN_REVIEW, ADDITIONAL_INFO_REQUESTED, APPROVED, REJECTED and any other applicable state, but not DRAFT applications that the user has not submitted yet.
- When the staff approves an application, create the new registration in the registration + related tables.

## Application Locking
The final states of an application is APPROVED or REJECTED.
Once the application is moved to a final state, an application will be locked and no further updates will be allowed.

Note: Once the application payment is successful, the client UI has to disable any further editing. API should also allow only a
staff user to make updates to a submitted application (document upload, state change to ADDITIONAL_INFO_REQUESTED)
