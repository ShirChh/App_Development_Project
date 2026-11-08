from flask import Flask, render_template, request, redirect, url_for
from Forms import CreateUserForms
from database import DatabaseHelper
from User import User

app = Flask(__name__)

db_helper = DatabaseHelper()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contactUs')
def contact_us():
    return render_template('contactUs.html')

@app.route('/createUser', methods = ['GET', 'POST'])
def create_user():
    create_user_form = CreateUserForms(request.form)
    if request.method == 'POST' and create_user_form.validate():
        try:
            #insert user into database
            user_id = db_helper.insert_user(
                first_name = create_user_form.first_name.data,
                last_name = create_user_form.last_name.data,
                gender = create_user_form.gender.data,
                membership = create_user_form.membership.data,
                remarks = create_user_form.remarks.data or ""
            )
            # Retrieve the user to confirm storage
            user_data = db_helper.get_user_by_id(user_id)
            if user_data:
                user = User.from_database_row(user_data)
                print(f"{user.get_first_name()} {user.get_last_name()} was stored in database "
                      f"successfully with user_id == {user.get_user_id()}")
                return redirect(url_for('home'))
        except Exception as e:
            print(f"Error storing user: {e}")

    return render_template('createUser.html', form = create_user_form)

@app.route('/retrieveUsers')
def retrieve_users():
    """Display all users from the database"""
    try: 
        users_data = db_helper.get_all_users()
        users_list = [User.from_database_row(row) for row in users_data]
        return render_template('retrieveUsers.html', users_list=users_list)
    except Exception as e:
        print(f"Error retrieving users: {e}")
        return render_template('retrieveUsers.html', users_list=[])

@app.route('/updateUser/<int:id>/', methods=['GET', 'POST'])
def update_user(id):
    update_user_form = CreateUserForms(request.form)
    
    if request.method == 'POST' and update_user_form.validate():
        # Handle form submission - update user in database
        try:
            success = db_helper.update_user(
                user_id=id, 
                first_name=update_user_form.first_name.data, 
                last_name=update_user_form.last_name.data, 
                gender=update_user_form.gender.data, 
                membership=update_user_form.membership.data, 
                remarks=update_user_form.remarks.data or "" 
            )
            if success:
                # Verify the update
                user_data = db_helper.get_user_by_id(id)
                if user_data:
                    user = User.from_database_row(user_data)
                    print(f"User {user.get_first_name()} {user.get_last_name()} was updated successfully with user_id == {user.get_user_id()}")
                return redirect(url_for('retrieve_users'))
            else: 
                print(f"Failed to update user with id {id}")
                # ADDED MISSING RETURN
                return render_template('updateUser.html', form=update_user_form)
        except Exception as e:
            print(f"Error updating user: {e}")
            return render_template('updateUser.html', form=update_user_form)
            
    # FIXED INDENTATION AND CHANGED TO ELIF
    elif request.method == 'GET':
        # Handle GET request - populate form with existing user data
        try:
            user_data = db_helper.get_user_by_id(id)
            if user_data:
                user = User.from_database_row(user_data)
                # Populate form with existing user data
                update_user_form.first_name.data = user.get_first_name()
                update_user_form.last_name.data = user.get_last_name()
                update_user_form.gender.data = user.get_gender()
                update_user_form.membership.data = user.get_membership()
                update_user_form.remarks.data = user.get_remarks()
                return render_template('updateUser.html', form=update_user_form, user=user)
            else:
                print(f"User with id {id} not found")
                return redirect(url_for('retrieve_users')) 
        except Exception as e:
            print(f"Error retrieving user: {e}")
            return redirect(url_for('retrieve_users'))
            
    # ADDED FALLBACK RETURN (Executes if POST request validation fails)
    return render_template('updateUser.html', form=update_user_form)

@app.route('/deleteUser/<int:id>', methods = ['POST'])
def delete_user(id):
    try:
        success = db_helper.delete_user(id)
        if success:
            print(f"User with ID {id} was deleted successfully")
        else:
            print(f"Failed to delete user with ID {id}")
    except Exception as e:
        print(f"Error deleting user: {e}")
    return redirect(url_for('retrieve_users'))
        
if __name__ == '__main__':
    app.run()