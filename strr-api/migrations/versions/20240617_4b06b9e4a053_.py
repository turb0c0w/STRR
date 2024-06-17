"""empty message

Revision ID: 4b06b9e4a053
Revises: 4298c4cb3f07
Create Date: 2024-06-17 00:54:23.116694

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '4b06b9e4a053'
down_revision = '4298c4cb3f07'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('event_records',
                    sa.Column('id', sa.INTEGER(),
                              autoincrement=True, nullable=False),
                    sa.Column('user_id', sa.INTEGER(),
                              autoincrement=False, nullable=True),
                    sa.Column('event_type', sa.VARCHAR(),
                              autoincrement=False, nullable=False),
                    sa.Column('message', sa.VARCHAR(),
                              autoincrement=False, nullable=False),
                    sa.Column('created_date', postgresql.TIMESTAMP(),
                              autoincrement=False, nullable=False, server_default=sa.text('(NOW())')),
                    sa.ForeignKeyConstraint(
                        ['user_id'], ['users.id'], name='event_records_user_id_fkey')
                    )
    op.create_table('invoices',
                    sa.Column('id', sa.INTEGER(),
                              autoincrement=True, nullable=False),
                    sa.Column('registration_id', sa.INTEGER(),
                              autoincrement=False, nullable=False),
                    sa.Column('invoice_id', sa.INTEGER(),
                              autoincrement=False, nullable=True),
                    sa.Column('payment_status_code', sa.VARCHAR(),
                              autoincrement=False, nullable=True),
                    sa.Column('payment_completion_date', postgresql.TIMESTAMP(
                    ), autoincrement=False, nullable=True),
                    sa.Column('payment_account', sa.VARCHAR(),
                              autoincrement=False, nullable=True),
                    sa.ForeignKeyConstraint(['registration_id'], [
                        'registrations.id'], name='invoices_registration_id_fkey')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('invoices')
    op.drop_table('event_records')
    # ### end Alembic commands ###
