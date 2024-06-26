<script lang="ts">
  import CreateReportCondensed from '$components/CreateReportCondensed.svelte';
  import { invalidAuth, isSignInModalOpen, isForgotPasswordModalOpen, isCreateAccountModalOpen, signedIn} from '$lib/stores';
  import avatar_icon from '$lib/images/avatar_icon.png';
  import target_icon from '$lib/images/target_icon.png';
  import type { PageData } from './$types';
  
	export let data: PageData;
  console.log(data);

  if (data.session?.user) {
    signedIn.set(true)
  }
  else if (data.failedAuth) {
    if (data.failedPath === "forgot") {
      isForgotPasswordModalOpen.set(true);
      invalidAuth.set(true);
    }
    else if (data.failedPath === "create") {
      isCreateAccountModalOpen.set(true);
      invalidAuth.set(true);
    }
    else {
      isSignInModalOpen.set(true);
      invalidAuth.set(true);
    }
  }

</script>

<main class="flex h-full flex-col gap-8 pb-8 text-center overflow-y-auto overflow-x-auto min-h-screen">
  <CreateReportCondensed/> 

  <!-- Horizontal Line -->
  <hr class="horizontal-line mt-24">

  <!-- Stats -->
  <div class="stats shadow mt-15" style="min-height: 116px; min-width: auto;">
    <div class="stat">
      <div class="stat-figure text-secondary">
        <div class="avatar {$signedIn ? 'online' : 'offline'}">
          <div class="w-16 rounded-full">
            <img alt="Avatar Icon" src="{avatar_icon}" />
          </div>
        </div>
      </div>
      {#if data.access}
        <div class="stat-value">{data.UserData.user_report_count}</div>
      {:else}
        <div class="stat-value">--</div>
      {/if}
      <div class="stat-title"># total de reportes tuyos</div>
    </div>
    
    <div class="stat">
      <div class="stat-figure text-primary">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="inline-block w-8 h-8 stroke-current"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"></path></svg>
      </div>
      <div class="stat-title"># total de reportes</div>
      <div class="stat-value text-primary">25.6K</div>
      <div class="stat-desc">21% más que el mes pasado</div>
    </div>
    
    <div class="stat">
      <div class="stat-figure text-secondary">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="inline-block w-8 h-8 stroke-current"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
      </div>
      <div class="stat-title"># de reportes resueltos</div>
      <div class="stat-value text-secondary">38</div>
      <div class="stat-desc">25% más que el mes pasado</div>
    </div>
  </div>

  <!-- My Reports Table -->
  <h1 class="font-bold text-4xl flex flex-start ml-48 mt-10">Tus Reportes</h1>
  <div class="reports-table-container">
    <div class="overflow-x-auto flex justify-center w-full h-full" style="{data.access ? '' : 'filter: blur(6px);'}">
      <table class="table w-3/4">
        <!-- head -->
        <thead>
          <tr>
            <th></th>
            <th>Categoría</th>
            <th>Municipio</th>
            <th>Resuelto</th>
          </tr>
        </thead>
        <tbody>
          {#if !data.access}
            <!-- row 1 -->
            <tr class="{data.access ? 'hover' : ''}">
              <th>1</th>
              <td>Poste caído</td>
              <td>Añasco</td>
              <td>Yes</td>
            </tr>
            <!-- row 2 -->
            <tr class="{data.access ? 'hover' : ''}">
              <th>2</th>
              <td>Carretera dañada</td>
              <td>Mayagüez</td>
              <td>No</td>
            </tr>
            <!-- row 3 -->
            <tr class="{data.access ? 'hover' : ''}">
              <th>3</th>
              <td>Edificio abandonado</td>
              <td>Mayagüez</td>
              <td>--</td>
            </tr>
          {:else if data.UserData.user_reports}
            {#each data.UserData.user_reports as report, i}
                <tr class="{data.access ? 'hover' : ''}">
                  <th>{report[7]}</th>
                  <td>{report[3]}</td>
                  <td>{report[2]}</td>
                  <td>No</td>
                </tr>
            {/each}
          {/if}
        </tbody>
      </table>
    </div>
    {#if !data.access}
      <div class="overlay-button text-lg">
        <button class="label-text-alt link text-base mr-2 text-accent" on:click={()=>$isCreateAccountModalOpen = true}>Crear una cuenta</button>
        o
        <button class="label-text-alt link link-hover text-lg ml-2 font-bold text-accent" on:click={()=>$isSignInModalOpen =true}>Iniciar Sesión</button>
      </div>
    {/if}
  </div>
  
  <!-- Horizontal Line -->
  <hr class="horizontal-line mt-56">

  <!-- Phone Mockup -->
  <div class="try-app w-full pl-48">
    <div class="mockup-phone border-secondary w-2/5">
      <div class="camera"></div> 
      <div class="display min-w-full">
        <div class="artboard artboard-demo phone-1 min-w-full">
          <button class="btn btn-lg btn-square btn-primary btn-disabled">
            <div class="w-20 h-20 overflow-hidden">
              <img alt="Theme Icon" src="{target_icon}" />              
            </div>
            <!-- <h1 class="text-info">Press to detect location</h1> -->
          </button>
        </div>
      </div>
    </div>
    <div class="try-app-text w-full mt-24">
      <h1 class="text-5xl font-bold" style="white-space: nowrap;">¡Trata nuestro app!</h1>
      <p class="mt-5">Encuentra nuestra applicación en el App Store y el Play Store</p>
      <button class="btn btn-info mt-10 ml-56" style="white-space: nowrap;">Pronto...</button>
    </div>
  </div>
  
</main>

<style lang="postcss">
  
  .horizontal-line {
    border: none;
    border-bottom: 1px solid oklch(var(--b2));  
  }
  .reports-table-container {
    position: relative;
    
  }
  .try-app {
    display: flex;
    justify-content: flex-start;
    position: sticky;
  }
  .overlay-button {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%); /* Center the button */
    z-index: 2; /* Ensure the button appears on top of the blurred element */
  }
  .try-app-text {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
</style>