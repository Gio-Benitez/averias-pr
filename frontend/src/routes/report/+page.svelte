<script lang="ts">
    import { Stepper, Step } from '@skeletonlabs/skeleton';
	import ReportCatDropdown from '$components/ReportCatDropdown.svelte';
	import EmailAddressInput from '$components/EmailAddressInput.svelte';
	function onCompleteHandler(e: Event): void { 
		console.log('event:complete', e); 
	}
	function onStepHandler(e: {detail: {state: {current: number, total: number}, step: number}}): void {
		console.log('event:step', e);
	}

</script>

<main class="flex h-full flex-col gap-8 pb-8 text-center">
	<h1>Submit a Report</h1>
    <Stepper  on:step={onStepHandler} >
		<!--Step 1: Enter Email Address-->
        <Step >
			<!--Header text for Step 1-->
			<svelte:fragment slot="header">
				Enter your Email Address
			</svelte:fragment>
			<!--Body text for Step 1-->
			<p>
				Enter your email address below to receive updates on your report.
			</p>
			
			<!--Input field for email address-->
			<EmailAddressInput />
        </Step>
		<!--Step 2: Select Report Category-->
    	<Step>
    		<svelte:fragment slot="header">
				Select a Report Category
			</svelte:fragment>
    		<!--Report Category Dropdown Component-->
			<ReportCatDropdown />

    	</Step>
		<!--Step 3-->
    	<Step>
    		<svelte:fragment slot="header">(header)</svelte:fragment>
    		(content)
    	</Step>
    	<!-- ... -->
    </Stepper>
</main>
