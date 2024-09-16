dev:
	cd MysqlContainer && docker build -t my-mysql-image . && \
	docker run -d --name my-mysql-container -p 3306:3306 my-mysql-image

clean:
	docker stop my-mysql-container
	docker rm my-mysql-container
	docker rmi my-mysql-image

git:
	git add .
	git commit -m "update"
	git push

fillDatabase:
	python3 insert_orders.py