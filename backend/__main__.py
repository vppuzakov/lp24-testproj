import logging

from backend.app import app

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging.DEBUG)
    logger.info("application started")
    app.run(host='0.0.0.0', port=8000, debug=False)


if __name__ == '__main__':
    main()
