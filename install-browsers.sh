#!/usr/bin/bash


# Enter the list of browsers to be downloaded
### Using Chromium as documented here - https://www.chromium.org/getting-involved/download-chromium
### https://commondatastorage.googleapis.com/chromium-browser-snapshots/index.html
chrome="https://www.googleapis.com/download/storage/v1/b/chromium-browser-snapshots/o/Linux_x64%2F1116103%2Fchrome-linux.zip?generation=1678562407182025&alt=media"
driver="https://www.googleapis.com/download/storage/v1/b/chromium-browser-snapshots/o/Linux_x64%2F1116103%2Fchromedriver_linux64.zip?generation=1678562412615699&alt=media"


mkdir -p "/opt/chrome"
curl -Lo /opt/chrome/chrome-linux.zip "$chrome"
unzip -q "/opt/chrome/chrome-linux.zip" -d "/opt/chrome"
rm /opt/chrome/chrome-linux.zip

mkdir -p "/opt/driver"
curl -Lo /opt/driver/chrome-driver.zip "$driver"
unzip -q "/opt/driver/chrome-driver.zip" -d /opt/driver
mv /opt/driver/chromedriver_linux64/chromedriver /opt/driver/
rm -rf /opt/chrome-driver/chrome-driver.zip /opt/chrome-driver/chromedriver_linux64
