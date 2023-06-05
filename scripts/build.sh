#!/bin/bash

# Import utils
. "$(dirname "$0")/utils.sh"

# Configuration
OS_NAME=$(get_os_name)
BUILD_DIR=./build
MAIN_FILE=./main.py
FILENAME=frigate
ICON_PATH=./assets/frigate.png
GLOBAL_FLAG="--onefile --standalone --follow-imports --output-dir=${BUILD_DIR} --enable-plugin=pyside6 --disable-console"
WINDOWS_FLAG="--output-filename=${FILENAME}-windows.exe --windows-icon-from-ico=${ICON_PATH}"
LINUX_FLAG="--output-filename=${FILENAME}-linux --linux-icon=${ICON_PATH}"
MACOS_FLAG="--output-filename=${FILENAME}-macos --macos-create-app-bundle --macos-app-icon=${ICON_PATH}"

function build_app() {
    case $OS_NAME in
        linux)
            python -m nuitka ${MAIN_FILE} ${GLOBAL_FLAG} ${LINUX_FLAG} || return 1
            ;;
        macos)
            python -m nuitka ${MAIN_FILE} ${GLOBAL_FLAG} ${MACOS_FLAG} || return 1
            ;;
        windows)
            python -m nuitka ${MAIN_FILE} ${GLOBAL_FLAG} ${WINDOWS_FLAG} || return 1
            ;;
        *)
            raise_an_error "ERROR: Can't build app for ${OS_NAME} system."
            ;;
    esac
    return 0 
}

echo -e "🔨 Initiate build for ${OS_NAME}\n"
build_app || raise_an_error "\n⛔ Build failed"
echo -e "\n✅ Build success"
