from app import manager

port = int(os.environ.get('PORT', 5000))

if __name__ == "__main__":
    manager.run(host='0.0.0.0', debug=True, port=port)