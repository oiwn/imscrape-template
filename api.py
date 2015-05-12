from utils.api_factory import ApiFactory


app = ApiFactory.get_instance()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
