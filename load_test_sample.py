from locust import HttpLocust, TaskSet, task

class MyTaskSet(TaskSet):

    @task(1)
    def task1(self):
        self.client.get("/story/news/nation-now/2016/07/05/scotland-oldest-organ-donor/86709054/")
   
class MyLocust(HttpLocust):
    task_set = MyTaskSet
