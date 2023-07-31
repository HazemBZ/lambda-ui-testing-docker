# Install Browser, OS dependencies and Python modules
# FROM public.ecr.aws/lambda/python@sha256:9cc6f47de700608ee0420246dac500edd34d059174ff0f7ea54f5230bda4e537 as lambda-base
### Python 3.8 has openssl issues with urllib3
FROM public.ecr.aws/lambda/python:3.11-x86_64 as lambda-base 

# Install dependencies
RUN yum install xz atk cups-libs gtk3 libXcomposite alsa-lib tar \
    libXcursor libXdamage libXext libXi libXrandr libXScrnSaver \
    libXtst pango at-spi2-atk libXt xorg-x11-server-Xvfb \
    xorg-x11-xauth dbus-glib dbus-glib-devel unzip bzip2 xdpyinfo -y -q

FROM lambda-base as dependencies-build

COPY install-browsers.sh /tmp/

# Install Browsers
RUN /usr/bin/bash /tmp/install-browsers.sh

# Remove not needed packages
RUN yum remove xz tar unzip bzip2 -y


FROM dependencies-build as py-build
# Install Python dependencies for function
COPY requirements.txt /tmp/
RUN pip install --upgrade pip -q
RUN pip install -r /tmp/requirements.txt -q

# Used by xvfb-run to determine xauth path
RUN yum install which -y -q



#
# Final image with code and dependencies
FROM py-build

COPY hosts /etc/hosts

COPY app.py /var/task
CMD [ "app.lambda_handler" ]

COPY entrypoint.sh /var/task

ENTRYPOINT ["bash", "/var/task/entrypoint.sh"]
