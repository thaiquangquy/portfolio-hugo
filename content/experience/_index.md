---
title: "Experience"
description: "My professional journey"
layout: "simple"
---

<style>
.sec-layout {
  display: flex;
  gap: 2.5rem;
  align-items: flex-start;
}
.sec-nav {
  width: 130px;
  flex-shrink: 0;
  position: sticky;
  top: 5rem;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}
.sec-nav-btn {
  display: block;
  width: 100%;
  padding: 0.5rem 1rem;
  border: 1px solid rgba(128,128,128,0.3);
  border-radius: 0.5rem;
  background: transparent;
  cursor: pointer;
  text-align: left;
  font-size: 0.875rem;
  color: inherit;
  transition: all 0.15s ease;
}
.sec-nav-btn:hover {
  border-color: rgba(128,128,128,0.6);
  background: rgba(128,128,128,0.1);
}
.sec-nav-btn.active {
  background: rgba(99,102,241,0.12);
  border-color: rgba(99,102,241,0.6);
  color: rgb(99,102,241);
  font-weight: 600;
}
.sec-panel { display: none; }
.sec-panel.active { display: block; text-decoration: none; }
.sec-table {
  width: 100%;
  border-collapse: collapse;
}
.sec-table th {
  padding: 0.5rem 0.75rem;
  text-align: left;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  opacity: 0.55;
  border-bottom: 1px solid rgba(128,128,128,0.25);
}
.sec-table td {
  padding: 0.65rem 0.75rem;
  border-bottom: 1px solid rgba(128,128,128,0.15);
  vertical-align: middle;
}
.sec-table tr:last-child td { border-bottom: none; }
.sec-table td, .sec-table td * { text-decoration: none !important; white-space: nowrap }
.sec-table a { color: rgb(99,102,241); white-space: nowrap; }
.sec-table a:hover { text-decoration: underline !important; }
.edu-chips {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-top: 1.25rem;
}
.edu-chip {
  padding: 0.25rem 0.7rem;
  border-radius: 9999px;
  border: 1px solid rgba(128,128,128,0.3);
  font-size: 0.8rem;
}
@media (max-width: 600px) {
  .sec-layout { flex-direction: column; }
  .sec-nav { width: 100%; flex-direction: row; position: static; top: auto; }
  .sec-nav-btn { flex: 1; text-align: center; }
  .sec-table td, .sec-table td * { white-space: normal !important; }
  .sec-table a { white-space: normal; }
}
</style>
<div class="not-prose sec-layout">
<div style="flex:1; min-width:0; margin-top:30px">
<div id="experience" class="sec-panel active">
<div style="overflow-x:auto;">
<table class="sec-table">
<thead>
<tr>
<th>Company</th>
<th>Link</th>
<th>Role</th>
<th>Dates</th>
<th>Location</th>
</tr>
</thead>
<tbody>
<tr>
<td><img src="/img/personify_logo.png" alt="Personify Inc Vietnam" style="height:28px; display:block;"></td>
<td><a href="https://personifyinc.com" target="_blank" rel="noopener">personifyinc.com</a></td>
<td>Team Leader</td>
<td>2020 – Present</td>
<td>Ho Chi Minh City</td>
</tr>
<tr>
<td><img src="/img/bosch_logo.svg" alt="Robert Bosch Engineering Vietnam" style="height:28px; display:block;"></td>
<td><a href="https://www.bosch.com" target="_blank" rel="noopener">bosch.com</a></td>
<td>Team Leader</td>
<td>2017 – 2020</td>
<td>Ho Chi Minh City</td>
</tr>
<tr>
<td><img src="/img/i3_logo.svg" alt="i3 International Inc" style="height:28px; display:block;"></td>
<td><a href="https://www.i3international.com" target="_blank" rel="noopener">i3international.com</a></td>
<td>Software Engineer</td>
<td>2016 – 2017</td>
<td>Ho Chi Minh City</td>
</tr>
</tbody>
</table>
</div>
</div>
<div id="education" class="sec-panel">
<div style="overflow-x:auto;">
<table class="sec-table">
<thead>
<tr>
<th>Institution</th>
<th>Degree</th>
<th>Years</th>
<th>Location</th>
</tr>
</thead>
<tbody>
<tr>
<td>Ho Chi Minh City University of Technology</td>
<td>B.Eng. Computer Science &amp; Engineering</td>
<td>2011 – 2016</td>
<td>Ho Chi Minh City</td>
</tr>
</tbody>
</table>
</div>
<div class="edu-chips">
<span class="edu-chip">Microchip Student Scholarship 2016</span>
<span class="edu-chip">ETS TOEIC 770</span>
<span class="edu-chip">Data Structures &amp; Algorithms</span>
<span class="edu-chip">Operating Systems</span>
<span class="edu-chip">Networking</span>
</div>
</div>
</div>
<nav class="sec-nav">
<button class="sec-nav-btn active" onclick="switchSection('experience', this)">Experience</button>
<button class="sec-nav-btn" onclick="switchSection('education', this)">Education</button>
</nav>
</div>
<script>
function switchSection(id, btn) {
  document.querySelectorAll('.sec-panel').forEach(function(p) { p.classList.remove('active'); });
  document.querySelectorAll('.sec-nav-btn').forEach(function(b) { b.classList.remove('active'); });
  document.getElementById(id).classList.add('active');
  btn.classList.add('active');
}
</script>
