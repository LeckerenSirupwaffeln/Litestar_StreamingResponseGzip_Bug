# set base image (host OS)
FROM python:3.11-slim

# expose the used ports
EXPOSE 8000

# set the working directory
WORKDIR /TestServer

# install bash
RUN apt-get update \
&& apt-get upgrade \
&& apt-get install -y --no-install-recommends sudo \
&& apt-get install -y --no-install-recommends bash \
&& apt-get install -y --no-install-recommends git \
&& apt-get install -y --no-install-recommends vim \
&& apt-get purge -y --auto-remove \
&& rm -rf /var/lib/apt/lists/*

# copy the content of the repo to our working directory
COPY . ./

# make scripts executable
RUN chmod +x ./scripts/entry.sh

# install dependencies
RUN pip install -e .

# create a non-root user and switch to it, for security.
RUN addgroup --system --gid 1001 "app-user"
RUN adduser --system --uid 1001 "app-user"
RUN chown -R app-user .
USER "app-user"

# Set default shell of app-user to bash
ENV SHELL /bin/bash

# command to run on container start
ENTRYPOINT ["/bin/sh", "-c"]
CMD ["./scripts/entry.sh"]