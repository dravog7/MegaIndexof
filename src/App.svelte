<script>
    import { Router, Link, Route } from "svelte-routing";
    import Navbar from "./components/navbar.svelte";

    import Construction from "./pages/Construction.svelte";
    import Specials from "./pages/specials.svelte";
    import About from "./pages/about.svelte";
    import Blog from "./pages/blog.svelte";
    import Education from "./pages/education.svelte";
    import Games from "./pages/games.svelte";
    import Projects from "./pages/projects.svelte";
    import Work from "./pages/work.svelte";
    export let url = "";
</script>

<style lang="text/postcss">

</style>
<Router url="{url}">
  <Navbar/>
  <Route path="/" component="{Construction}" />
  <Route path="/special" component="{Specials}"/>
  <Route path="/about" component="{About}"/>
  <Route path="/blog" component="{Blog}"/>
  <Route path="/games" component="{Games}"/>
  <Route path="/projects" component="{Projects}"/>
  <Route path="/work" component="{Work}"/>
  <Route path="/education" component="{Education}"/>
</Router>