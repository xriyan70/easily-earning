from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Earn Pro</title>

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">

<style>
body{
margin:0;
font-family:Poppins;
background:#f1f5f9;
}

/* TOP */
.top{
background:#fff;
padding:15px;
display:flex;
justify-content:space-between;
font-weight:700;
}

/* TASK */
.task{
background:#fff;
margin:10px;
padding:15px;
border-radius:15px;
display:flex;
justify-content:space-between;
}

.btn{
background:#77e621;
border:none;
padding:8px 15px;
border-radius:20px;
font-weight:700;
}

/* REFER */
.card{
background:#fff;
margin:10px;
padding:15px;
border-radius:15px;
text-align:center;
}

/* WITHDRAW */
.withdraw{
background:#fff;
margin:10px;
padding:15px;
border-radius:15px;
}

/* NAV */
.nav{
position:fixed;
bottom:0;
width:100%;
background:#fff;
display:flex;
justify-content:space-around;
padding:10px;
}

.nav div{
text-align:center;
font-size:12px;
}

.active{
color:#77e621;
}

.page{
display:none;
}

.show{
display:block;
}

input{
width:100%;
padding:12px;
margin-top:10px;
border-radius:10px;
border:1px solid #ccc;
}

</style>
</head>

<body>

<div class="top">
<div>Earn Pro</div>
<div>৳0</div>
</div>

<!-- HOME -->
<div id="home" class="page show">

<div class="task">
<div>
<b>Official Task 1</b><br>
৳15 Reward
</div>
<button class="btn">Start</button>
</div>

<div class="task">
<div>
<b>Official Task 2</b><br>
৳10 Reward
</div>
<button class="btn">Start</button>
</div>

<div class="task">
<div>
<b>Official Task 3</b><br>
৳20 Reward
</div>
<button class="btn">Start</button>
</div>

</div>

<!-- REFER -->
<div id="refer" class="page">

<div class="card">
<b>Refer & Earn</b><br><br>

৳5 per refer<br>
Friend completes 2 tasks → ৳5<br>
Extra 5% commission
</div>

<button class="btn" style="width:90%;margin:10px;">
Refer Now
</button>

</div>

<!-- WITHDRAW -->
<div id="withdraw" class="page">

<div class="withdraw">

<select style="width:100%;padding:10px;">
<option>৳100</option>
<option>৳200</option>
<option>৳500</option>
</select>

<input placeholder="Enter Number">

<button class="btn" style="width:100%;margin-top:10px;">
Withdraw
</button>

</div>

<div class="withdraw">
<b>Live Withdraw</b>
<div id="live"></div>
</div>

</div>

<!-- NAV -->
<div class="nav">

<div onclick="show('home')" class="active">Tasks</div>
<div onclick="show('refer')">Refer</div>
<div onclick="show('withdraw')">Withdraw</div>

</div>

<script>

function show(id){
document.querySelectorAll('.page').forEach(p=>p.classList.remove('show'))
document.getElementById(id).classList.add('show')
}

function live(){
let names=["Maruf","Siyam","Hasan","Jihad"]
let amt=[100,200,500]

let n=names[Math.floor(Math.random()*names.length)]
let a=amt[Math.floor(Math.random()*amt.length)]

document.getElementById('live').innerHTML =
"<div>"+n+" withdrew ৳"+a+"</div>" + document.getElementById('live').innerHTML
}

setInterval(live,3000)

</script>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html)

app.run(host="0.0.0.0", port=5000)
