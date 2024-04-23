<script>
    import electrical_pole_icon from '$lib/images/electric_pole.png';
    import landslide_icon from '$lib/images/landslide_icon.png';
    import landslidehazard_icon from '$lib/images/landslidehazard_icon.png';
    import lightning_icon from '$lib/images/lightning_icon.png';
    import pothole_icon from '$lib/images/pothole_icon.png';
    import water_drop_icon from '$lib/images/water_drop_icon.png';
</script>


<div class="flex flex-row justify-center">
    <button class="btn btn-lg btn-square btn-primary">
        <div class="w-20 h-20 overflow-hidden">
          <img alt="Lightining Icon" src="{lightning_icon}" />              
        </div>
        ¡No tengo luz!    
    </button>

    <button class="btn btn-lg btn-square btn-primary">
        <div class="w-20 h-20 overflow-hidden">
          <img alt="Water Drop Icon" src="{water_drop_icon}" />              
        </div>
        ¡No tengo agua!    
    </button>

    <button class="btn btn-lg btn-square btn-primary">
        <div class="w-20 h-20 overflow-hidden">
          <img alt="Pothole Icon" src="{pothole_icon}" />              
        </div>
        Pothole   
    </button>
</div>
<div class="flex flex-row justify-center">
    <button class="btn btn-lg btn-square btn-primary">
        <div class="w-20 h-20 overflow-hidden">
          <img alt="Electrical Pole Icon" src="{electrical_pole_icon}" />              
        </div>
        Fallen Electrical Pole    
    </button>

    <button class="btn btn-lg btn-square btn-primary">
        <div class="w-20 h-20 overflow-hidden">
          <img alt="Landslide Icon" src="{landslide_icon}" />              
        </div>
        Landslide   
    </button>

    <button class="btn btn-lg btn-square btn-primary">
        <div class="w-20 h-20 overflow-hidden">
          <img alt="Potential Landslide Icon" src="{landslidehazard_icon}" />              
        </div>
        Landslide Hazard   
    </button>
</div>