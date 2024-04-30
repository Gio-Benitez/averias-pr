<script>
  import { steps_counter } from "$lib/stores";
</script>



{#if $steps_counter===1}
    <div class="flex justify-center align-middle w-full mb-20">
        <ul class="steps sm:steps-vertical lg:steps-horizontal w-full" style="z-index:-1;">
            <li class="step step-primary text-sm">Detectar Ubicación</li>
            <li class="step text-sm">Seleccionar Categoría</li>
            <li class="step text-sm">Subir Imágen</li>
            <li class="step text-sm">Crear Reporte</li>
        </ul>
    </div>
{/if}

{#if $steps_counter===2}
    <div class="flex justify-center w-full mb-20">
        <ul class="steps sm:steps-vertical lg:steps-horizontal w-full" style="z-index:-1;">
            <li class="step step-primary text-sm">Detectar Ubicación</li>
            <li class="step step-primary text-sm">Seleccionar Categoría</li>
            <li class="step text-sm">Subir Imágen</li>
            <li class="step text-sm">Crear Reporte</li>
        </ul>
    </div>
{/if}

{#if $steps_counter===3}
    <div class="flex justify-center w-full mb-20">
        <ul class="steps sm:steps-vertical lg:steps-horizontal w-full" style="z-index:-1;">
            <li class="step step-primary text-sm">Detectar Ubicación</li>
            <li class="step step-primary text-sm">Seleccionar Categoría</li>
            <li class="step step-primary text-sm">Subir Imágen</li>
            <li class="step text-sm">Crear Reporte</li>
        </ul>
    </div>
{/if}

{#if $steps_counter>=4}
    <div class="flex justify-center w-full mb-20">
        <ul class="steps sm:steps-vertical lg:steps-horizontal w-full" style="z-index:-1;">
            <li class="step step-primary text-sm">Detectar Ubicación</li>
            <li class="step step-primary text-sm">Seleccionar Categoría</li>
            <li class="step step-primary text-sm">Subir Imágen</li>
            <li class="step step-success text-sm text-success">Crear Reporte</li>
        </ul>
    </div>
{/if}
