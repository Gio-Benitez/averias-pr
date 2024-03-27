<!-- Navigation Bar Svelte Component -->
  <nav class="navbar">
    <!-- Section containing the -->
    <section class="grid-cols-6 flex items-center">
      <a href="/" class="flex items-center bg-slate ml-8 mr-2">AveriasPR</a>
      <a href="/map" class="flex items-center bg-slate ml-8 mr-2">Map</a>
      <a href="/dashboard" class="flex items-center bg-slate ml-8 mr-2">Dashboard</a>
      <a href="/report" class="flex items-center bg-slate ml-8 mr-2" style="white-space: nowrap;"> Create a Report</a>
      <section class="dropdown dropdown-end dropdown-bottom w-full py-4 pr-8 ml-8 mr-2">
        <button>Theme</button>
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
    </section>
    <a href="/account" class="flex items-center bg-slate mr-5">Sign In</a>
    
  </nav>

  <style>
    .navbar{
      display: flex;
      justify-content: space-between;
    }
  </style>
