<script>
import { onMount } from 'svelte';
let view=false;
onMount(async ()=>{
    let pass=prompt("enter pass");
    if(pass=="rose")
        view=true;
});
</script>
<style lang="text/postcss">
.content {
    @apply w-screen;
    display: flex;
}
.content:nth-child(odd) {
    min-height: 20%;
}
.content:nth-child(even) {
    min-height: 40%;
    background-attachment: fixed;
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
}

#img1 {
    background-image: url("https://www.w3schools.com/howto/img_parallax.jpg");
    min-height: 100%;
}
#img3 {
    background-image: url("https://www.w3schools.com/howto/img_parallax2.jpg");
    min-height: 50%;
}
#img5 {
    background-image: url("https://www.w3schools.com/howto/img_parallax3.jpg");
    min-height: 50%;
}
#img7 {
    background-image: url("https://www.w3schools.com/howto/img_parallax.jpg");
    min-height: 100%;
}
.font-pacific {
    font-family: 'Pacifico';
}
</style>
{#if view}
<div class="block font-pacific">
    <div class="w-screen h-16">
    </div>
    <div class="content" id="img1">
    <span class="m-auto">
    Lorem, ipsum dolor sit amet consectetur adipisicing elit. Animi culpa iure tempore, reprehenderit, nesciunt ipsum expedita, perspiciatis similique perferendis consequatur distinctio possimus? Et magnam, dolores culpa aperiam odio dolorum eaque!
    </span>
    </div>
    <div class="content bg-blue-400">
    Lorem, ipsum dolor sit amet consectetur adipisicing elit. Animi culpa iure tempore, reprehenderit, nesciunt ipsum expedita, perspiciatis similique perferendis consequatur distinctio possimus? Et magnam, dolores culpa aperiam odio dolorum eaque!
    </div>
    <div class="content" id="img3">
    <span>
    Lorem, ipsum dolor sit amet consectetur adipisicing elit. Animi culpa iure tempore, reprehenderit, nesciunt ipsum expedita, perspiciatis similique perferendis consequatur distinctio possimus? Et magnam, dolores culpa aperiam odio dolorum eaque!
    </span>
    </div>
    <div class="content bg-pink-400">
    Lorem, ipsum dolor sit amet consectetur adipisicing elit. Animi culpa iure tempore, reprehenderit, nesciunt ipsum expedita, perspiciatis similique perferendis consequatur distinctio possimus? Et magnam, dolores culpa aperiam odio dolorum eaque!
    </div>
    <div class="content" id="img5">
    <span>
    Lorem, ipsum dolor sit amet consectetur adipisicing elit. Animi culpa iure tempore, reprehenderit, nesciunt ipsum expedita, perspiciatis similique perferendis consequatur distinctio possimus? Et magnam, dolores culpa aperiam odio dolorum eaque!
    </span>
    </div>
    <div class="content bg-purple-400">
    Lorem, ipsum dolor sit amet consectetur adipisicing elit. Animi culpa iure tempore, reprehenderit, nesciunt ipsum expedita, perspiciatis similique perferendis consequatur distinctio possimus? Et magnam, dolores culpa aperiam odio dolorum eaque!
    </div>
    <div class="content" id="img7">
    <span class="m-auto">
    Lorem, ipsum dolor sit amet consectetur adipisicing elit. Animi culpa iure tempore, reprehenderit, nesciunt ipsum expedita, perspiciatis similique perferendis consequatur distinctio possimus? Et magnam, dolores culpa aperiam odio dolorum eaque!
    </span>
    </div>
</div>
{:else}
<div class="m-auto">
    Nothing to see here
</div>
{/if}