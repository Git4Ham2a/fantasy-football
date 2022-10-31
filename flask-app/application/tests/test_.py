# Import the necessary modules
from flask import url_for
from flask_testing import TestCase
from . import app, db
from . import Teams, Players

# import the app's classes and objects
from application.models import Teams, Players

#Creating the base class
class TestBase(TestCase):
    def create_app(self):

        #Pass in testing configuration for the app.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db", SECRET_KEY='TEST_SECRET_KEY', DEBUG=True, WTF_CSRF_ENABLED=False)
        return app

# Called before every test
    def setUp(self):
        #Create table 
        db.create_all()
        # Create test team 
        test_team = Teams(name="Test-Team")
        # save to database
        db.session.add(test_team)
        db.session.commit() 
        # Create test player
        test_player = Players(name = "Test-Player", position = "Test-Position", fk_teamid = test_team.id)
        db.session.add(test_player)
        db.session.commit() 

# Called after every test
    def tearDown(self):
        db.session.remove()
        db.drop_all()

# Test sending a GET request for the index.html page
class TestIndexPage(TestBase):
    def test_index_get(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Index page test', response.data)

#Test sending a GET request to the add player page 
class TestAddPlayer1(TestBase):
    def test_addplayer_get(self):
        response = self.client.get(url_for('addplayer'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Create test: player 1', response.data)

#Test adding a player
class TestAddPlayer2(TestBase):
    def test_addplayer_get(self):
        response = self.client.post(url_for('addplayer', id=1), data = dict(name='Test-Create-Player'), follow_redirects=True)
        self.assertIn(b'Ceate test: player 2', response.data)

#Test sending a GET request to the add team page 
class TestAddTeam1(TestBase):
    def test_addteam_get(self):
        response = self.client.get(url_for('addteam'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Create test: team 1', response.data)

#Test adding a team
class TestAddTeam2(TestBase):
    def test_addteam_get(self):
        response = self.client.post(url_for('addteam'), data = dict(name="Test-Create-Team"), follow_redirects=True)
        self.assertIn(b'Create test: team 2',response.data)

#Test sending a GET request to update the player page 
class TestUpdatePlayer1(TestBase):
    def test_updateplayer1(self):
        response = self.client.get(url_for('updateplayer', id=1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Update test: player 1', response.data)

#Test updating a player 
class TestUpdatePlayer2(TestBase):
    def test_updateplayer2(self):
        response = self.client.post(url_for('updateplayer'), data = dict(name="Test-Update-Player"), follow_redirects=True)
        self.assertIn(b'Update test: player 2', response.data)

#Test sending a GET request to update the team page 
class TestUpdateTeam1(TestBase):
    def test_updateteam1(self):
        response = self.client.get(url_for('updateteam', id=1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Update test: team 1', response.data)

#Test updating a team 
class TestUpdateTeam2(TestBase):
    def test_updateteam2(self):
        response = self.client.post(url_for('updateteam'), data = dict(name="Test-Update-Team"), follow_redirects=True)
        self.assertIn(b'Update test: team 2', response.data)

#Test deleting a player from database
class TestDeletePlayer(TestBase):    
    def test_deleteplayer(self):
        response = self.client.get(url_for('deleteplayer', id = 1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Delete test: team', response.data)
        self.assertNotIn(b'Delete test: player', response.data)

#Test deleting a team from database
class TestDeleteTeams(TestBase):
    def test_deleteteam(self):
        response = self.client.get(url_for('deleteteam', id = 1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'Delete test: team ', response.data)
