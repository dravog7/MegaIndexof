<script>
import { link } from "svelte-routing";
import {getContext} from 'svelte';
import {ROUTER} from 'svelte-routing/src/contexts';
import Ham from './hamburger.svelte'
var { activeRoute } = getContext(ROUTER);
let expanded=0;
let currRoute;
$: {
    if($activeRoute){
        currRoute = $activeRoute.uri;
    console.log($activeRoute);
    }
}
</script>

<style lang="text/postcss">
a:hover, a:visited, a:link, a:active{
    color: black;
    text-decoration: none;
}

.nav {
    opacity: 0.75;
}

.nav:hover {
    opacity: 1;
}

li {
    @apply p-4;
}
</style>

<div class="nav font-mono fixed bg-gray-200 rounded-r-lg lg:w-screen">
    <div class="lg:hidden p-4">
    <Ham on:switch="{e=>expanded=!e.detail.state}"/>
    </div>
    <ol class:hidden={!expanded} class="lg:flex">
        <li class:border-b-4="{$activeRoute?currRoute=='/':false}" class="border-red-400"><a href="/" use:link>Home</a></li>
        <li class:border-b-4="{$activeRoute?currRoute=='/about':false}" class="hidden border-orange-400"><a href="/about" use:link>About</a></li>
        <li class:border-b-4="{$activeRoute?currRoute=='/education':false}" class="hidden border-yellow-400"><a href="/education" use:link>Education</a></li>
        <li class:border-b-4="{$activeRoute?currRoute=='/work':false}" class="hidden border-green-400"><a href="/work" use:link>Work Experience</a></li>
        <li class:border-b-4="{$activeRoute?currRoute=='/projects':false}" class="hidden border-teal-400"><a href="/projects" use:link>Projects</a></li>
        <li class:border-b-4="{$activeRoute?currRoute=='/games':false}" class="hidden border-blue-400"><a href="/games" use:link>Games</a></li>
        <li class:border-b-4="{$activeRoute?currRoute=='/blog':false}" class="hidden border-indigo-400"><a href="/blog" use:link>Blog</a></li>
        <li class:border-b-4="{$activeRoute?currRoute=='/special':false}" class="border-purple-400"><a href="/special" use:link>Specials</a></li>
    </ol>
</div>