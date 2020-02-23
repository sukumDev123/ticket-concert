from Actor.models import ActorModel
from ticket_consert.CallBack import CallBack


class ActorPresenter:

    def find_actor_all(self):
        try:
            actors = ActorModel.objects.all()
            return actors
        except Exception as e:
            print("find actor all err: ", e)
            return e

    def find_actor_by_id_actor(self, actor_id):
        return ActorModel.objects.get(id_actor=actor_id)

    def delete_by_id_actor(self, id_actor):
        try:
            self.find_actor_by_id_actor(id_actor).delete()
            return True
        except Exception as e:
            print("find actor all err: ", e)
            return e
