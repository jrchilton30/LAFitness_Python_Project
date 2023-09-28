# Jack Chilton, CIS 345, 12-1:15PM, Project Class File

class Member:
    def __init__(self, gym_id, ball_status=0, fine=0):
        self.gym_id = gym_id
        self.ball_status = ball_status
        self.fine = fine

    @property
    def ball_status(self):
        return self._ball_status

    @ball_status.setter
    def ball_status(self, new_ball_status):
        self._ball_status = new_ball_status

    @property
    def fine(self):
        return self._fine

    @fine.setter
    def fine(self, fine):
        self._fine = fine

    def __str__(self):
        return self.gym_id
