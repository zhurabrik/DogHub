#################################################################
####################### BUILD STAGE #############################
#################################################################
# This image contains:
# 1. All the Python versions
# 2. required python headers
# 3. C compiler and developer tools
FROM snakepacker/python:all as builder

# Create virtualenv on python 3.9
# Target folder should be the same on the build stage and on the target stage
RUN python3.9 -m venv /usr/share/python3/app
RUN apt update
RUN apt install -y libpq-dev

COPY requirements.txt /tmp/
RUN /usr/share/python3/app/bin/pip install -Ur /tmp/requirements.txt

# Install target package
ADD . /tmp/dogshub
RUN /usr/share/python3/app/bin/pip install -U '/tmp/dogshub'

# Will be find required system libraries and their packages
RUN find-libdeps /usr/share/python3/app > /usr/share/python3/app/pkgdeps.txt

#################################################################
####################### TARGET STAGE ############################
#################################################################
# Use the image version used on the build stage
FROM snakepacker/python:3.9

# Copy virtualenv to the target image
COPY --from=builder /usr/share/python3/app /usr/share/python3/app

# Install the required library packages
RUN cat /usr/share/python3/app/pkgdeps.txt | xargs apt-install

# Create a symlink to the target binary (just for convenience)
RUN ln -snf /usr/share/python3/app/bin/dogshub-api /usr/bin/

CMD ["dogshub-api"]