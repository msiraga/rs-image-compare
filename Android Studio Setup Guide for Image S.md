# Android Studio Setup Guide for Image Slider App

This guide provides detailed instructions for setting up Android Studio and creating an emulator to test the Image Slider application.

## Installing Android Studio

1. **Download Android Studio**
   - Go to [https://developer.android.com/studio](https://developer.android.com/studio)
   - Download the latest version (Android Studio Meerkat or newer)
   - Run the installer

2. **Installation Process**
   - Choose "Standard" installation type when prompted
   - This will install:
     - Android SDK
     - Android SDK Platform
     - Android Virtual Device (emulator)
   - Click "Next" and "Finish" to complete installation

3. **First Launch Setup**
   - Launch Android Studio
   - Accept the license agreements when prompted
   - Wait for initial components to download
   - Sign in with Google account (optional)

## Gradle Configuration

If you encounter Java/Gradle compatibility issues:

1. **Update Gradle Version**
   - Go to File > Project Structure
   - Select "Project" on the left panel
   - Change Gradle Version to 8.10
   - Click "Apply" and "OK"

2. **Alternative: Edit Gradle Wrapper Properties**
   - Navigate to android/gradle/wrapper/gradle-wrapper.properties
   - Update the distributionUrl to:
     ```
     distributionUrl=https\://services.gradle.org/distributions/gradle-8.10-all.zip
     ```

3. **Sync Project**
   - Click the "Sync Project with Gradle Files" button (elephant icon with arrow)
   - Wait for the sync to complete

## Setting Up an Android Emulator

1. **Open Device Manager**
   - Click on "Tools" in the top menu
   - Select "Device Manager"

2. **Create a Virtual Device**
   - Click the "Create device" button
   - This opens the "Virtual Device Configuration" wizard

3. **Select Hardware**
   - Choose a device definition (recommended: Pixel 6)
   - Click "Next"

4. **Select System Image**
   - Choose the "Recommended" tab
   - Select a recent Android version (Android 13 or newer)
   - If not downloaded, click the "Download" link next to it
   - Wait for download to complete
   - Click "Next"

5. **Configure the Virtual Device**
   - Name your AVD (Android Virtual Device) or keep the default
   - Recommended settings:
     - Enable "Device Frame" for realistic device appearance
     - Set "Startup orientation" to Portrait
     - Keep "Graphics" set to Automatic
   - Click "Finish"

6. **Start the Emulator**
   - In Device Manager, find your newly created virtual device
   - Click the "Play" button (triangle) next to it
   - Wait for the emulator to boot (may take 1-2 minutes)

## Running the Image Slider App on the Emulator

1. **Ensure Project is Ready**
   - Make sure Gradle sync has completed successfully
   - Verify the project builds without errors

2. **Run the App**
   - Click the green "Run" button in the toolbar (or press Shift+F10)
   - Select your running emulator from the device selection dialog
   - Click "OK"

3. **Testing App Features**
   - Test the image comparison slider functionality
   - Test camera integration (emulator has a simulated camera)
   - Verify dark/light theme toggle works
   - Test all interactive elements

## Troubleshooting Common Issues

1. **Emulator Won't Start**
   - Ensure Hyper-V is enabled in BIOS
   - Verify you have at least 4GB of RAM available
   - Try reducing emulator memory in AVD settings

2. **App Crashes on Launch**
   - Check Logcat in Android Studio for error details
   - Verify Capacitor plugins are correctly configured
   - Run `npx cap sync` to ensure web assets are up to date

3. **Camera Not Working**
   - Grant camera permissions when prompted
   - For emulator: use the emulator's camera controls
   - For physical device: ensure camera hardware is functioning

4. **Performance Issues**
   - Close unnecessary applications to free up memory
   - In emulator settings, reduce window size or use a less demanding device profile
   - Consider using a physical device for final testing

## Updating the App After Web Code Changes

1. Update your web code (HTML, CSS, JS)
2. Run `npx cap sync` to update the Android project
3. In Android Studio, click "Sync Project with Gradle Files"
4. Run the app again to see your changes

## Preparing for Release

1. **Generate Signed APK/Bundle**
   - Go to Build > Generate Signed Bundle/APK
   - Follow the wizard to create a signing key
   - Choose APK or Android App Bundle (recommended)

2. **Configure Release Build**
   - Set build variant to "release"
   - Optimize code and resources

3. **Test Release Version**
   - Install the generated APK on a test device
   - Verify all functionality works as expected

4. **Publish to Google Play**
   - Create a Google Play Developer account
   - Follow the submission process on the Google Play Console