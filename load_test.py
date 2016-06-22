from locust import HttpLocust, TaskSet, task

class MyTaskSet(TaskSet):

    @task(1)
    def task1(self):
        self.client.get("/v4/content/22781415%2C%2022782659%2C%2022696533?consumer=stage_load_test")

    @task(1)
    def task2(self):
        self.client.get("/v4/assets/22781415%2C%2022782659%2C%2022696533?consumer=stage_load_test")
    
    @task(1)
    def task2(self):
        self.client.get("/v4/blogs/1/cruiselog?frontname=news&sitereferrerid=1&consumer=ak")
   
    @task(1)
    def task2(self):
        self.client.get("/v4/fronts/1/home_mobile?sitereferrerid=1&merged=true&consumer=stage_load_test&merged=false")
   
    @task(1)
    def task2(self):
        self.client.get("/v4/fronts/1/home_mobile?sitereferrerid=1&merged=true&consumer=stage_load_test&merged=true")
   
    @task(1)
    def task2(self):
        self.client.get("/v4/fronts/topics/9740db96-14ca-41e5-89dc-8ac8f6544b7e/1?sitereferrerid=1&consumer=stage_load_test")
    
    @task(1)
    def task2(self):
        self.client.get("/v4/search/1?frontName=home_mobile&sitereferrerid=1&livefrontqueue=false&consumer=stage_load_test")
   
class MyLocust(HttpLocust):
    task_set = MyTaskSet
