---
title: "Services"
description: "Software consulting, programming courses, and interview prep with Quy Thai Quang"
layout: "simple"
---

<style>
.svc-root, .svc-root * { text-decoration: none !important; }
.svc-intro { margin-top: 0.5rem; opacity: 0.8; max-width: 42rem; }
.svc-stats { display: flex; flex-wrap: wrap; gap: 2rem; margin-top: 1.25rem; font-size: 0.875rem; opacity: 0.85; }
.svc-stats b { display: block; font-size: 1.25rem; }
.svc-tabs {
  position: sticky;
  top: 0;
  z-index: 10;
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-top: 2rem;
  padding: 0.75rem 0;
  border-bottom: 1px solid rgba(128,128,128,0.25);
  background: rgb(var(--color-neutral));
}
.dark .svc-tabs { background: rgb(var(--color-neutral-800)); }
.svc-tab {
  padding: 0.5rem 1rem;
  min-height: 44px;
  border: 1px solid rgba(128,128,128,0.3);
  border-radius: 9999px;
  background: transparent;
  color: inherit;
  font-size: 0.9rem;
  cursor: pointer;
  transition: all 0.15s ease;
}
.svc-tab:hover { background: rgba(128,128,128,0.1); }
.svc-tab.active { background: rgb(var(--color-primary-600)); border-color: rgb(var(--color-primary-600)); color: #fff; font-weight: 600; }
.svc-panel { display: none; padding-top: 2rem; }
.svc-panel.active { display: block; }
.svc-head { display: flex; justify-content: space-between; align-items: flex-end; flex-wrap: wrap; gap: 1rem; margin-bottom: 1.5rem; }
.svc-head h2 { margin: 0; font-size: 1.6rem; font-weight: 700; }
.svc-head p { margin: 0.25rem 0 0; opacity: 0.75; max-width: 38rem; }
.svc-lang { display: inline-flex; border: 1px solid rgba(128,128,128,0.3); border-radius: 0.5rem; overflow: hidden; font-size: 0.8rem; }
.svc-lang button { padding: 0.3rem 0.75rem; background: transparent; color: inherit; border: 0; cursor: pointer; opacity: 0.6; }
.svc-lang button.active { background: rgba(128,128,128,0.15); opacity: 1; font-weight: 600; }
.svc-tiers { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1rem; }
.svc-tier {
  position: relative;
  display: flex;
  flex-direction: column;
  padding: 1.5rem;
  border: 1px solid rgba(128,128,128,0.3);
  border-radius: 0.875rem;
}
.svc-tier.pop { border-color: rgb(var(--color-primary-500)); box-shadow: 0 0 0 1px rgb(var(--color-primary-500)); }
.svc-flag { position: absolute; top: -0.7rem; left: 1.5rem; padding: 0.1rem 0.65rem; border-radius: 9999px; background: rgb(var(--color-primary-600)); color: #fff; font-size: 0.75rem; }
.svc-tier h3 { margin: 0; font-size: 1.1rem; font-weight: 700; }
.svc-sub { margin: 0.15rem 0 1rem; font-size: 0.875rem; opacity: 0.7; }
.svc-price { font-size: 1.9rem; font-weight: 700; }
.svc-price small { font-size: 0.85rem; font-weight: 400; opacity: 0.7; }
.dark .dark .svc-row { display: flex; align-items: center; gap: 0.6rem; min-height: 1.5rem; margin-bottom: 0.1rem; }
.svc-tag { padding: 0.1rem 0.55rem 0.1rem 0.95rem; border-radius: 0 0.25rem 0.25rem 0; background: rgba(22,163,74,0.14); color: rgb(21,128,61); font-size: 0.75rem; font-weight: 700; letter-spacing: 0.02em; line-height: 1.4; clip-path: polygon(0.5rem 0, 100% 0, 100% 100%, 0.5rem 100%, 0 50%); }
.dark .svc-tag { background: rgba(34,197,94,0.18); color: rgb(134,239,172); }
.svc-root .svc-was { text-decoration: line-through !important; font-size: 0.95rem; opacity: 0.55; }
.svc-price { font-variant-numeric: tabular-nums; line-height: 1.15; }
.svc-save { margin-top: 0.25rem; font-size: 0.85rem; font-weight: 600; color: rgb(21,128,61); }
.dark .svc-save { color: rgb(134,239,172); }
.svc-ltd { font-weight: 400; opacity: 0.7; color: inherit; }
.svc-tier ul { flex: 1; list-style: none; margin: 1rem 0 1.5rem; padding: 0; font-size: 0.925rem; }
.svc-tier li { position: relative; padding: 0.2rem 0 0.2rem 1.5rem; }
.svc-tier li::before { content: "✓"; position: absolute; left: 0; color: rgb(var(--color-secondary-500)); }
.svc-badge { display: inline-block; margin-left: 0.4rem; padding: 0 0.5rem; border-radius: 9999px; font-size: 0.7rem; font-weight: 600; vertical-align: middle; }
.svc-badge.open { background: rgba(16,185,129,0.15); color: rgb(16,185,129); }
.svc-badge.wait { background: rgba(245,158,11,0.15); color: rgb(217,119,6); }
.svc-btn {
  display: block;
  padding: 0.6rem 1rem;
  border: 1px solid rgb(var(--color-primary-600));
  border-radius: 0.6rem;
  color: rgb(var(--color-primary-600));
  text-align: center;
  font-weight: 600;
  text-decoration: none !important;
}
.dark .svc-btn { border-color: rgb(var(--color-primary-400)); color: rgb(var(--color-primary-400)); }
.svc-btn:hover { background: rgba(128,128,128,0.1); }
.svc-btn.solid, .dark .svc-btn.solid { background: rgb(var(--color-primary-600)); border-color: rgb(var(--color-primary-600)); color: #fff; }
.svc-btn.solid:hover { background: rgb(var(--color-primary-700)); }
.svc-note { margin-top: 1rem; font-size: 0.85rem; opacity: 0.7; text-align: center; }
.svc-faq { margin-top: 3rem; padding-top: 1.5rem; border-top: 1px solid rgba(128,128,128,0.25); }
.svc-faq h2 { font-size: 1.3rem; font-weight: 700; margin: 0 0 1rem; }
.svc-faq details { margin-bottom: 0.5rem; padding: 0.75rem 1rem; border: 1px solid rgba(128,128,128,0.3); border-radius: 0.6rem; }
.svc-faq summary { cursor: pointer; font-weight: 600; }
.svc-faq details p { margin: 0.5rem 0 0; opacity: 0.75; }
.dark .dark @media (max-width: 640px) {
  .svc-stats { gap: 1.25rem; }
  .svc-tab { flex: 1; }
}
</style>
<div class="not-prose svc-root">
<p class="svc-intro">I've spent 10 years building backend and distributed systems at Bosch and Personify. Hire me for your system, or learn how to build one yourself.</p>
<div class="svc-stats">
<div><b>10+ yrs</b>production systems</div>
<div><b>Java · AWS</b>Spring Boot, Postgres</div>
<div><b>Team lead</b>hiring &amp; interviewing</div>
</div>
<div class="svc-tabs" role="tablist">
<button class="svc-tab active" data-panel="consulting" role="tab">💼 Consulting &amp; Servicing</button>
<button class="svc-tab" data-panel="courses" role="tab">📚 Programming Courses</button>
<button class="svc-tab" data-panel="interview" role="tab">🎯 Interview Course</button>
</div>
<div id="consulting" class="svc-panel active">
<div class="svc-head">
<div>
<h2>Consulting &amp; Servicing</h2>
<p>For startups and product teams that need a senior backend engineer without hiring full-time.</p>
</div>
</div>
<div class="svc-tiers">
<div class="svc-tier">
<h3>Architecture Review</h3>
<div class="svc-sub">One-off, fixed scope</div>
{{< price id="architecture" >}}
<ul>
<li>2-hr deep dive with your team</li>
<li>Written report: risks, bottlenecks, roadmap</li>
<li>Postgres &amp; AWS cost check</li>
<li>30-day follow-up call</li>
</ul>
<a class="svc-btn" href="mailto:quythai.dev@gmail.com?subject=Architecture%20Review">Book intro call</a>
</div>
<div class="svc-tier pop">
<span class="svc-flag">Most picked</span>
<h3>Fractional Tech Lead</h3>
<div class="svc-sub">Monthly retainer</div>
{{< price id="retainer" >}}
<ul>
<li>~40 hrs / month</li>
<li>Code review &amp; design decisions</li>
<li>Mentoring your dev team</li>
<li>Async Slack support, 24h response</li>
</ul>
<a class="svc-btn solid" href="mailto:quythai.dev@gmail.com?subject=Fractional%20Tech%20Lead">Book intro call</a>
</div>
<div class="svc-tier">
<h3>Build &amp; Ship</h3>
<div class="svc-sub">Project-based delivery</div>
{{< price id="build" >}}
<ul>
<li>Spring Boot / React / AWS</li>
<li>Milestones with fixed quotes</li>
<li>CI/CD, docs, handover</li>
<li>4 weeks of post-launch support</li>
</ul>
<a class="svc-btn" href="mailto:quythai.dev@gmail.com?subject=Build%20%26%20Ship">Book intro call</a>
</div>
</div>
<p class="svc-note">Hourly ad-hoc work: {{< price id="hourly" inline="true" >}} · Invoiced in USD · Remote, async-friendly (GMT+7)</p>
</div>
<div id="courses" class="svc-panel">
<div class="svc-head">
<div>
<h2 data-en="Programming Courses" data-vi="Khóa học lập trình">Programming Courses</h2>
<p data-en="Backend with Java &amp; Spring Boot, from fundamentals to production. Choose how you want to learn." data-vi="Lập trình Backend với Java &amp; Spring Boot, từ nền tảng đến production. Chọn cách học phù hợp với bạn.">Backend with Java &amp; Spring Boot, from fundamentals to production. Choose how you want to learn.</p>
</div>
<div class="svc-lang"><button class="active" data-lang="en">EN</button><button data-lang="vi">VI</button></div>
</div>
<div class="svc-tiers">
<div class="svc-tier">
<h3><span data-en="Self-paced" data-vi="Tự học">Self-paced</span><span class="svc-badge wait" data-en="Waitlist" data-vi="Sắp ra mắt">Waitlist</span></h3>
<div class="svc-sub" data-en="Video + exercises, lifetime access" data-vi="Video + bài tập, truy cập trọn đời">Video + exercises, lifetime access</div>
{{< price id="selfpaced" >}}
<ul>
<li data-en="40+ lessons" data-vi="40+ bài học">40+ lessons</li>
<li data-en="Real project: job-queue service" data-vi="Dự án thật: dịch vụ job-queue">Real project: job-queue service</li>
<li data-en="Community Discord" data-vi="Cộng đồng Discord">Community Discord</li>
</ul>
<a class="svc-btn" href="mailto:quythai.dev@gmail.com?subject=Waitlist%3A%20Self-paced%20course" data-en="Join waitlist" data-vi="Đăng ký chờ">Join waitlist</a>
</div>
<div class="svc-tier pop">
<span class="svc-flag" data-en="Next cohort: Jan 2027" data-vi="Khóa tới: 01/2027">Next cohort: Jan 2027</span>
<h3><span data-en="Live Cohort" data-vi="Lớp Live">Live Cohort</span><span class="svc-badge open" data-en="Open" data-vi="Đang mở">Open</span></h3>
<div class="svc-sub" data-en="8 weeks, max 12 students" data-vi="8 tuần, tối đa 12 học viên">8 weeks, max 12 students</div>
{{< price id="cohort" >}}
<ul>
<li data-en="2 live sessions / week" data-vi="2 buổi live / tuần">2 live sessions / week</li>
<li data-en="Code review on every assignment" data-vi="Review code mọi bài tập">Code review on every assignment</li>
<li data-en="Everything in Self-paced" data-vi="Bao gồm gói Tự học">Everything in Self-paced</li>
</ul>
<a class="svc-btn solid" href="mailto:quythai.dev@gmail.com?subject=Enroll%3A%20Live%20Cohort" data-en="Enroll now" data-vi="Đăng ký ngay">Enroll now</a>
</div>
<div class="svc-tier">
<h3><span data-en="1:1 Mentoring" data-vi="Mentor 1:1">1:1 Mentoring</span><span class="svc-badge open" data-en="Open" data-vi="Đang mở">Open</span></h3>
<div class="svc-sub" data-en="Personal plan around your goals" data-vi="Lộ trình riêng theo mục tiêu của bạn">Personal plan around your goals</div>
{{< price id="mentoring" >}}
<ul>
<li data-en="4 × 60-min calls" data-vi="4 buổi × 60 phút">4 × 60-min calls</li>
<li data-en="Async questions between calls" data-vi="Hỏi đáp giữa các buổi">Async questions between calls</li>
<li data-en="Career &amp; project review" data-vi="Review dự án &amp; định hướng">Career &amp; project review</li>
</ul>
<a class="svc-btn" href="mailto:quythai.dev@gmail.com?subject=1%3A1%20Mentoring" data-en="Pick a slot" data-vi="Chọn lịch">Pick a slot</a>
</div>
</div>
</div>
<div id="interview" class="svc-panel">
<div class="svc-head">
<div>
<h2 data-en="Interview Course" data-vi="Khóa luyện phỏng vấn">Interview Course</h2>
<p data-en="Prep taught by someone who runs the interviews: coding, system design, and the behavioral round." data-vi="Luyện phỏng vấn cùng người trực tiếp phỏng vấn tuyển dụng: coding, system design và vòng behavioral.">Prep taught by someone who runs the interviews: coding, system design, and the behavioral round.</p>
</div>
<div class="svc-lang"><button class="active" data-lang="en">EN</button><button data-lang="vi">VI</button></div>
</div>
<div class="svc-tiers">
<div class="svc-tier">
<h3><span data-en="Interview Playbook" data-vi="Cẩm nang phỏng vấn">Interview Playbook</span><span class="svc-badge wait" data-en="Waitlist" data-vi="Sắp ra mắt">Waitlist</span></h3>
<div class="svc-sub" data-en="Self-paced guide + question bank" data-vi="Tự học + ngân hàng câu hỏi">Self-paced guide + question bank</div>
{{< price id="playbook" >}}
<ul>
<li data-en="150 curated questions" data-vi="150 câu hỏi chọn lọc">150 curated questions</li>
<li data-en="System design templates" data-vi="Template system design">System design templates</li>
<li data-en="CV checklist" data-vi="Checklist CV">CV checklist</li>
</ul>
<a class="svc-btn" href="mailto:quythai.dev@gmail.com?subject=Waitlist%3A%20Interview%20Playbook" data-en="Join waitlist" data-vi="Đăng ký chờ">Join waitlist</a>
</div>
<div class="svc-tier pop">
<span class="svc-flag" data-en="Best value" data-vi="Đáng giá nhất">Best value</span>
<h3><span data-en="Bootcamp" data-vi="Bootcamp">Bootcamp</span><span class="svc-badge open" data-en="Open" data-vi="Đang mở">Open</span></h3>
<div class="svc-sub" data-en="4-week live cohort" data-vi="Lớp live 4 tuần">4-week live cohort</div>
{{< price id="bootcamp" >}}
<ul>
<li data-en="Weekly live drills" data-vi="Luyện live hàng tuần">Weekly live drills</li>
<li data-en="2 mock interviews with feedback" data-vi="2 buổi phỏng vấn thử có nhận xét">2 mock interviews with feedback</li>
<li data-en="Includes Playbook" data-vi="Bao gồm Cẩm nang">Includes Playbook</li>
</ul>
<a class="svc-btn solid" href="mailto:quythai.dev@gmail.com?subject=Enroll%3A%20Interview%20Bootcamp" data-en="Enroll now" data-vi="Đăng ký ngay">Enroll now</a>
</div>
<div class="svc-tier">
<h3><span data-en="Mock Interview" data-vi="Phỏng vấn thử">Mock Interview</span><span class="svc-badge open" data-en="Open" data-vi="Đang mở">Open</span></h3>
<div class="svc-sub" data-en="1:1, single session" data-vi="1:1, một buổi">1:1, single session</div>
{{< price id="mock" >}}
<ul>
<li data-en="Realistic coding or design round" data-vi="Vòng coding hoặc design như thật">Realistic coding or design round</li>
<li data-en="Written scorecard" data-vi="Bảng đánh giá chi tiết">Written scorecard</li>
<li data-en="EN or VI" data-vi="Tiếng Anh hoặc tiếng Việt">EN or VI</li>
</ul>
<a class="svc-btn" href="mailto:quythai.dev@gmail.com?subject=Mock%20Interview" data-en="Pick a slot" data-vi="Chọn lịch">Pick a slot</a>
</div>
</div>
</div>
<div class="svc-faq">
<h2>Questions</h2>
<details><summary>How do payments work?</summary><p>Consulting: USD invoice (Wise/bank). Courses: VND bank transfer or card.</p></details>
<details><summary>Can my company pay for my course?</summary><p>Yes, I can issue an invoice to your employer.</p></details>
<details><summary>Refunds?</summary><p>Full refund before the second cohort session.</p></details>
</div>
</div>
<script>
(function() {
  var tabs = document.querySelectorAll('.svc-tab');
  function show(id) {
    tabs.forEach(function(t) { t.classList.toggle('active', t.dataset.panel === id); });
    document.querySelectorAll('.svc-panel').forEach(function(p) { p.classList.toggle('active', p.id === id); });
  }
  tabs.forEach(function(t) {
    t.addEventListener('click', function() {
      show(t.dataset.panel);
      history.replaceState(null, '', '#' + t.dataset.panel);
    });
  });
  var hash = location.hash.slice(1);
  if (document.getElementById(hash) && document.getElementById(hash).classList.contains('svc-panel')) show(hash);
  document.querySelectorAll('.svc-lang').forEach(function(group) {
    group.querySelectorAll('button').forEach(function(b) {
      b.addEventListener('click', function() {
        var lang = b.dataset.lang;
        group.querySelectorAll('button').forEach(function(x) { x.classList.toggle('active', x === b); });
        group.closest('.svc-panel').querySelectorAll('[data-en]').forEach(function(el) { el.textContent = el.dataset[lang]; });
      });
    });
  });
})();
</script>
