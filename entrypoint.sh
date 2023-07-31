#!/bin/bash
export DISPLAY=:25

xvfb-run -e /dev/stdout -s "-screen 0 1280x1024x24 -ac -nolisten tcp -nolisten unix"  /lambda-entrypoint.sh app.lambda_handler

## Attempt 1  to ensure Xvfb is running
# /usr/bin/Xvfb "$DISPLAY" -screen 0 1280x800x24 -nolisten tcp -nolisten unix &
# Wait for Xvfb
# MAX_ATTEMPTS=120 # About 60 seconds
# COUNT=0
# echo -n "Waiting for Xvfb to be ready..."
# while ! xdpyinfo -display "$DISPLAY" >/dev/null 2>&1; do
#   echo -n "."
#   sleep 0.50s
#   COUNT=$(( COUNT + 1 ))
#   if [ "${COUNT}" -ge "${MAX_ATTEMPTS}" ]; then
#     echo "  Gave up waiting for X server on $DISPLAY"
#     exit 1
#   fi
# done
# echo "  Done - Xvfb is ready!"

