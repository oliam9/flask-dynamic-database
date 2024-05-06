from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Dubai, UAE',
        'salary': 'AED12000'
   },
    {
            'id': 2,
            'title': 'Tester',
            'location': 'Remote',
            'salary': 'E1500'
       },
    {
            'id': 3,
            'title': 'Front-End',
            'location': 'Dublin, Ireland',
            'salary': '&1200'
       },
    {
            'id': 4,
            'title': 'Full-Stack',
            'location': 'SF, California',
            'salary': '$4000'
       },
    {
            'id': 5,
            'title': 'Back-end',
            'location': 'London, UK',
            'salary': '&2500'
       },
]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)