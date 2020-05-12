import manage
if __name__ == "__main__":
    manage.app.run(host="0.0.0.0", threaded=True, port=80)