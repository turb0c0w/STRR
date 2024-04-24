#build stage
FROM node:18.17-bullseye-slim AS build
ENV PNPM_HOME="/pnpm"
ENV PATH="$PNPM_HOME:$PATH"
RUN corepack enable

COPY . /web
WORKDIR /web

RUN pnpm install
RUN pnpm build

#runtime stage
FROM nginx:1.25

COPY --from=build /web/strr-main-app/.output/public /usr/share/nginx/html/