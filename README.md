# Richdale AI Image Compare

A modern, responsive web app for comparing before/after images with a smooth slider interface.

Try it here: https://msiraga.github.io/rs-image-compare/

## Features
- Easy image upload
- Smooth sliding comparison
- Mobile-friendly design
- Installable as PWA (Progressive Web App)
- Works offline
- Dark/Light theme toggle
- Image adjustments:
  - Brightness control
  - Contrast control
  - Filter effects
- Export options:
  - Download comparison
  - Create video animation
  - Share link

# Image Comparison Slider

A powerful image comparison tool that works as:
- Web application
- Progressive Web App (PWA)
- Native iOS application
- Native Android application

## Features

- Interactive slider to compare before/after images
- Camera integration on mobile devices
- Share functionality
- Dark/light theme
- Responsive design
- Works offline
- Python backend for advanced image processing

## Setup Instructions

### Quick Setup

Run the `setup.bat` file to automatically set up the project:

```bash
setup.bat
```

### Manual Setup

1. **Python Environment Setup**:
   ```bash
   # Activate the virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate

   # Install Python dependencies
   pip install -r requirements.txt
   ```

2. **Node.js/Capacitor Setup**:
   ```bash
   # Install Node.js dependencies
   npm install

   # Initialize Capacitor
   npx cap init "Image Slider" "com.richdale.imageslider"

   # Create www directory and copy files
   mkdir www
   copy *.html *.js *.json *.png *.svg www\

   # Add platforms
   npx cap add android
   npx cap add ios
   ```

## Running the Application

### Web Application

```bash
# Start the Python Flask server
python app.py
```

Then open your browser to http://localhost:5000

### Native Android App

```bash
# Sync web content to native project
npx cap sync android

# Open in Android Studio
npx cap open android
```

In Android Studio:
1. Connect your device or start an emulator
2. Click the Run button

### Native iOS App

```bash
# Sync web content to native project
npx cap sync ios

# Open in Xcode
npx cap open ios
```

In Xcode:
1. Connect your device or select a simulator
2. Click the Run button

## Updating the Application

After making changes to the web files:

1. Copy updated files to www directory:
   ```bash
   copy *.html *.js *.json *.png *.svg www\
   ```

2. Sync with native projects:
   ```bash
   npx cap sync
   ```

## Troubleshooting

- **Slider not working**: Clear browser cache or reinstall the app
- **Images not loading**: Check file permissions and formats
- **Native features not working**: Ensure Capacitor plugins are properly installed

## Installation

### On Android
1. Open the app in Chrome
2. Tap the install button or menu (⋮)
3. Select "Install app" or "Add to Home Screen"

### On iOS
1. Open the app in Safari
2. Tap the Share button
3. Select "Add to Home Screen"

## How to Use
1. Upload a "before" image
2. Upload an "after" image
3. Use the slider to compare images
4. Adjust image settings (optional):
   - Change brightness/contrast
   - Apply filters
5. Create a video or download the comparison

## Development
- Built with vanilla JavaScript
- PWA-enabled with service workers
- Responsive design using CSS Grid/Flexbox
- GitHub Pages deployment ready

## Recent Updates
- Added dark/light theme toggle
- Improved mobile responsiveness
- Added image adjustment controls
- Enhanced PWA installation experience
- Added video creation feature
- Fixed GitHub Pages deployment issues

## License
MIT License - feel free to use and modify
MIT License