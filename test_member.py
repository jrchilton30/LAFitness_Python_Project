# Jack Chilton, CIS 345, 12-1:15PM, Project Class Auto Testing

from jrchilto_ProjectClass import *


class TestMember:
    def test_details(self):
        m = Member('0001')
        print('testing details: member')
        assert ('0001', 0, 0) == (m.gym_id, m.ball_status, m.fine)

    def test_ball_status(self):
        m = Member('0001')
        print('testing details: ball_status')
        m.ball_status = 1
        assert 1 == m.ball_status

    def test_fine(self):
        m = Member('0001')
        print('testing details: fine')
        m.fine = 60
        assert 60 == m.fine
