# This is where your CREATE, READ, UPDATE AND DELETE functionality is going to go. 
from asyncio import Task
from flask import render_template, url_for, redirect, request 
from application import app, db 
from application.models import Players, Teams
from application.forms import PlayerForm, TeamForm

#READ BOTH DATABASES
#Location of this functionality: ip_address:5000/
@app.route('/', methods=['POST', 'GET'])
def index():
    teams = Teams.query.all()
    players = Players.query.all()
    return render_template('index.html', title="Fantasy Football", teams=teams, players=players)

# CREATE team 
@app.route('/addteam', methods=['POST', 'GET'])
def teamadd():
    form = TeamForm() 
    if form.validate_on_submit(): 
        teams = Teams(
            name = form.name.data
        )
        db.session.add(teams)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('addteams.html', title="Add a new Team", form=form)

#CREATE player 
#Location of this functionality: ip_address:5000/add
@app.route('/addplayer', methods=['POST','GET'])
def add():
    # This points to TodoForm
    form = PlayerForm()
    # Checks that we have clicked the submit button
    if form.validate_on_submit():
        # the variable tasks becomes what is put on the form 
        # todos becomes what we are going to be adding to the database
        players = Players(
            name = form.name.data,
            position = form.position.data,
            # Foreign key as a option to add to the create process. 
            fk_teamid = form.fk_teamid.data
        )
        # This performs the add to database
        db.session.add(players)
        # This commits those changes
        db.session.commit()
        # This one redirects to the index functions url
        return redirect(url_for('index'))
    # Otherwise return the template of add.html
    return render_template('addplayer.html', title="Add a new Player", form=form)

#UPDATE teams 
@app.route('/updateteam/<int:id>', methods=['GET', 'POST'])
def updateteam(id):
    form = TeamForm()

    teams = Teams.query.get(id)

    if form.validate_on_submit():
        teams.name = form.name.data
        db.session.commit()
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.name.data = teams.name
    return render_template('updateteam.html', title='Update the player', form=form)


#UPDATE player
@app.route('/updateplayer/<int:id>', methods=['GET', 'POST'])
def update(id):
    form = PlayerForm()
    # Get one name from the specified ID
    name = Players.query.get(id)
    # POST method
    # If the user clicks submit
    if form.validate_on_submit():
        # What is put in the form gets ammended to the database
        name.name = form.name.data,
        name.position = form.position.data,
        name.fk_teamid = form.fk_teamid.data
        # Commit the changes
        db.session.commit()
        # Redirect to the url for index function 
        return redirect(url_for('index'))
    # Else if the request method is a GET
    elif request.method == 'GET':
        # Update the form with whats in the database
        form.name.data = name.name 
        form.position.data = name.position
        form.fk_teamid.data = name.fk_teamid
    # If we go to the url return the template updateplayer.html
    return render_template('updateplayer.html', title='Update the player', form=form)


#DELETE team
@app.route('/deleteteam/<int:id>')
def deletelist(id):
    team = Teams.query.get(id)
    db.session.delete(team)
    db.session.commit()
    return redirect(url_for('index'))

#DELETE player
#Location of this functionality: ip_address:5000/delete/1
@app.route('/deleteplayer/<int:id>')
def deleteplayer(id):
    # Collecting the task we want to delete based on its id
    name = Players.query.get(id)
    # deleting this item from the database
    db.session.delete(name)
    # committing this change
    db.session.commit()
    # returning the url in the index function. 
    return redirect(url_for('index'))
