<script>
import { onMount,onDestroy } from 'svelte';
import Loading from "../components/Loading.svelte"
import Navbar from "../components/navbar.svelte";
onMount(async () => {
    document.body.classList.add("construction");
});

onDestroy(async () => {
    document.body.classList.remove("construction");
});
</script>
<style lang="text/postcss">
.main {
    font-family: 'Pacifico';
    font-style: italic;
    font-size: 2rem;
}
</style>
<div class="font-mono flex m-auto text-center w-56 h-56 main">
    <span class="m-auto">Coming Soon!</span>
</div>