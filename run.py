from app import app

with app.app_context():
	import putorder
	import postorder
	import getgenorders


if __name__ == '__main__':
    app.run()
