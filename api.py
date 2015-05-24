from utils.api_factory import ApiFactory


api = ApiFactory.get_instance()


if __name__ == '__main__':
    api.run(host='0.0.0.0', port=8000)
