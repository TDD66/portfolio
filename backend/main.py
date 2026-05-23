import functions_framework
from google.cloud import firestore

db = firestore.Client(database="portfolio")

@functions_framework.http
def visitor_counter(request):

    if request.method == "OPTIONS":
        headers = {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET",
            "Access-Control-Allow-Headers": "Content-Type",
        }
        return ("", 204, headers)

    headers = {"Access-Control-Allow-Origin": "*"}

    counter_ref = db.collection("counters").document("visitors")
    counter_ref.update({"count": firestore.Increment(1)})
    doc = counter_ref.get()
    count = doc.to_dict().get("count", 0)

    return ({"count": count}, 200, headers)
