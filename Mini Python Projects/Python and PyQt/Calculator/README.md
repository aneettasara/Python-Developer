# Creating a Calculator With Python and PyQt

Here’s a step-by-step MVC design pattern for a GUI desktop Calculator application:

* The user performs an action or request (event) on the view (GUI).
* The view notifies the controller about the user’s action.
* The controller gets the user’s request and queries the model for a response.
* The model processes the controller query, performs the required operations, and returns an answer or result.
* The controller receives the model’s answer and updates the view accordingly.
* The user finally sees the requested result on the view.
