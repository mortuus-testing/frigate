if __name__ == '__main__':
    import sys
    from package import app

    exit_code = app.start(sys.argv)
    sys.exit(exit_code)
