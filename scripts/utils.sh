#!/bin/bash

# Utility function to get the os type
function get_os_name() {
    case "$OSTYPE" in
        solaris*) echo "solaris" ;;
        darwin*)  echo "macos" ;; 
        linux*)   echo "linux" ;;
        bsd*)     echo "bsd" ;;
        msys*)    echo "windows" ;;
        cygwin*)  echo "windows" ;;
        *)        echo "$OSTYPE" ;;
    esac
}

# Helper function to raise an error
function raise_an_error() {
    ERROR_MESSAGE=$1
    echo -e "$ERROR_MESSAGE"
    exit 1
}