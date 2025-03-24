@echo off
echo Setting up Image Slider project with native capabilities...

echo Activating Python virtual environment...
call venv\Scripts\activate

echo Installing Python dependencies...
pip install -r requirements.txt

echo Installing Node.js dependencies...
npm install

echo Creating www directory...
if not exist www mkdir www

echo Copying web assets to www directory...
copy *.html www\
copy *.js www\
copy *.json www\
copy *.png www\
copy *.svg www\
if exist *.jpeg copy *.jpeg www\
if exist *.jpg copy *.jpg www\

echo Initializing Capacitor...
npx cap init "Image Slider" "com.richdale.imageslider" --web-dir www

echo Adding platforms...
npx cap add android
npx cap add ios

echo Setup complete!
echo.
echo To run the web app: python app.py
echo To open Android Studio: npx cap open android
echo To open Xcode (on Mac): npx cap open ios
echo.
