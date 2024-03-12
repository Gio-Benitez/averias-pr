<!-- Navigation Bar Svelte Component -->
  <nav class="navbar">
    <!-- Section containing the -->
    <section class="grid-cols-5 gap-10">
      <a href="/" class="flex items-center bg-slate ml-8 mr-2">AveriasPR</a>
      <a href="/map" class="flex items-center bg-slate ml-8 mr-2">Interactive Map</a>
      <a href="/dashboard" class="flex items-center bg-slate ml-8 mr-2">Dashboard</a>
      <a href="/report" class="flex items-center bg-slate ml-8 mr-2">Report</a>
      <a href="/account" class="flex items-center bg-slate ml-8 mr-2">Account</a>
    </section>
    <section class="dropdown dropdown-end dropdown-bottom w-full py-4 pr-8">
      <button class="btn float-right">Theme</button>
      <ul tabIndex={1} class="menu dropdown-content rounded-box z-50 w-52 bg-base-100 p-2 shadow">
      <li>
        <option data-set-theme="light">Light</option>
      </li>
      <li>
        <option data-set-theme="dark">Dark</option>
      </li>
      <li>
        <option data-set-theme="cupcake">Cupcake</option>
      </li>
      <li>
        <option data-set-theme="retro">Retro</option>
      </li>
      <li>
        <option data-set-theme="corporate">Corporate</option>
      </li>
      <li>
        <option data-set-theme="business">Business</option>
      </li>
    </ul>
    </section>
  </nav>
