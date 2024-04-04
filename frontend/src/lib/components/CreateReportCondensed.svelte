
<div class="join" style="display: flex; justify-content: center; align-items: center; ">
    <!--Location Text Input **Change later to detect location button-->
    <input type="text" placeholder="Location" class="input input-bordered input-md w-1/8 max-w-xs" required />
    <!--Separator-->
    <div class="divider divider-horizontal">*</div>
    <!--Category Drop down-->
    <select class="select select-bordered w-1/8 max-w-xs">
      <option disabled selected>Category</option>
      <option>Pothole</option>
      <option>Lightpost</option>
      <option>Landslide/Potential Landslide</option>
      <option>Water Issues</option>
      <option>Electrical Service Issues</option>
    </select>
    <!--Separator-->
    <div class="divider divider-horizontal">*</div>
    <!--Image input-->
    <label class="form-control w-1/8 max-w-xs">
        <div class="label">
          <span class="label-text">Upload Image</span>
        </div>
        <input type="file" class="file-input file-input-bordered file-input-primary w-7/8 max-w-xs file-input-sm mb-9"/>
      </label>
    <!--Separator-->
    <div class="divider divider-horizontal">*</div>
    <!--Additional Notes Area-->
    <textarea class="textarea textarea-bordered w-1/8" placeholder="Additional Notes"></textarea>
    <!--Separator-->
    <div class="divider divider-horizontal">*</div>
    <!--Create Report Button-->
    <div style="display: flex; justify-content: center; align-items: center;">
        <a href="/report" style="text-align: center;">
          <button class="btn rounded-full btn-outline btn-success ml-15" style="white-space: nowrap; font-weight: bold;">Create Report</button>
        </a>
      </div>
  </div>

  