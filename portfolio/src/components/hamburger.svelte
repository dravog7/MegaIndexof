<script>
import { createEventDispatcher } from 'svelte';
const dispatch = createEventDispatcher();
let state=true;
let Cross;
let Ham;
function handleToggle() {
    if(state)
        Cross.beginElement();
    else
        Ham.beginElement();
    state=!state;
    dispatch("switch",{state});
}
</script>
<button class="w-8" on:click="{handleToggle}">
    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 100 60">
        <path id="shape" d="M 10 10 h 90 v 10 h -90 v -10 M 10 30 h 90 v 10 h -90 v -10 M 10 50 h 90 v 10 h -90 v -10" fill="black" stroke="black">
            <animate bind:this="{Cross}" id="toCross" attributeName="d" dur="0.1s" to="M 10 20 L 100 60 L 100 50 L 10 10 L 10 20 M 10 60 L 100 20 L 100 10 L 10 50 L 10 60" fill="freeze" begin="indefinite"/>
            <animate bind:this="{Ham}" id="toHam" attributeName="d" dur="0.1s" to="M 10 10 h 90 v 10 h -90 v -10 M 10 30 h 90 v 10 h -90 v -10 M 10 50 h 90 v 10 h -90 v -10" fill="freeze" begin="indefinite"/>
        </path>
    </svg>
</button>