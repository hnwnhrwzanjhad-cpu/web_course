const box=document.querySelector(".box");
box.addEventListener("mouseenter",function(){
    this.style.background ="red"
})
box.addEventListener("mouseleave",function(){
    this.style.background ="purple"
})