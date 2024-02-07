from flask import Flask, request, json
import status

# create the app instance
app = Flask(__name__)

COUNTERS = {}


@app.route("/counters/<name>", methods=["POST", "PUT", "GET", "DELETE"])
def create_counter(name):
    """create a counter"""

    global COUNTERS

    if request.method == "POST":

        app.logger.info(f"Rquest to create a counter: {name}")

        if name not in COUNTERS:
            # add the new counter
            COUNTERS[name] = {"sell": 0, "left": 0}

        else:
            return {
                "message": f"counter {name} already exists"
            }, status.HTTP_409_CONFLICT

        return {name: COUNTERS[name]}, status.HTTP_201_CREATED

    elif request.method == "PUT":

        app.logger.info(f"Rquest to update the counter: {name}")

        if name not in COUNTERS:
            COUNTERS[name] = {"sell": 0, "left": 0}

        # get data from request
        data = json.loads(request.data)
        # update the inventory levels
        COUNTERS[name]["sell"] = data["sell"]
        COUNTERS[name]["left"] = data["left"]

        return {name: COUNTERS[name]}, status.HTTP_200_OK

    elif request.method == "GET":

        app.logger.info(f"Rquest to get the counter: {name}")

        if name not in COUNTERS:
            return {
                "message": f"Counter is not created : {name}"
            }, status.HTTP_404_NOT_FOUND

        return {name: COUNTERS[name]}, status.HTTP_200_OK

    elif request.method == "DELETE":

        app.logger.info(f"Rquest to delete the counter: {name}")

        if name in COUNTERS:
            del COUNTERS[name]
            return {"message": "deletion successful ..."}, status.HTTP_204_NO_CONTENT

        else:
            return {"message": "deletetion failed ..."}, status.HTTP_404_NOT_FOUND
