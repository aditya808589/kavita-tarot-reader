/**
 * KAVITA — Celestial Ice Crystal Dust Effect
 * Pure brilliant white ice + dark obsidian crystal particles + stardust gold sheen.
 * Runs smoothly at 60fps across both dark and light sections of the website.
 */
(function() {
  function initIceEffect() {
    let canvas = document.getElementById('kavitaIceCanvas');
    if (!canvas) {
      canvas = document.createElement('canvas');
      canvas.id = 'kavitaIceCanvas';
      canvas.style.cssText = 'position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:9998;';
      document.body.prepend(canvas);
    }

    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    let width = canvas.width = window.innerWidth;
    let height = canvas.height = window.innerHeight;

    window.addEventListener('resize', () => {
      width = canvas.width = window.innerWidth;
      height = canvas.height = window.innerHeight;
    }, { passive: true });

    const particleCount = window.innerWidth < 768 ? 42 : 78;
    const particles = [];

    // Particle types:
    // 0: Pure Brilliant White Ice (luminous, glowing)
    // 1: Dark Obsidian / Cosmic Crystal (crisp contrast on white/cream sections)
    // 2: Warm Stardust Gold (spiritual luxury warmth)
    for (let i = 0; i < particleCount; i++) {
      const typeRand = Math.random();
      let type = 0; // default pure white
      if (typeRand < 0.42) {
        type = 0; // 42% Pure White Ice
      } else if (typeRand < 0.78) {
        type = 1; // 36% Dark Celestial Ice (visible on light backgrounds)
      } else {
        type = 2; // 22% Sacred Warm Gold
      }

      particles.push({
        x: Math.random() * width,
        y: Math.random() * height,
        radius: Math.random() * 2.0 + 1.1, // 1.1px to 3.1px circular particles
        speedY: Math.random() * 0.45 + 0.22, // Slow gentle descent
        speedX: (Math.random() - 0.5) * 0.26,
        opacity: Math.random() * 0.45 + 0.35,
        pulse: Math.random() * Math.PI * 2,
        pulseSpeed: Math.random() * 0.024 + 0.012,
        type: type
      });
    }

    let isVisible = true;
    document.addEventListener('visibilitychange', () => {
      isVisible = !document.hidden;
    });

    function render() {
      if (!isVisible) {
        requestAnimationFrame(render);
        return;
      }

      ctx.clearRect(0, 0, width, height);

      for (let i = 0; i < particles.length; i++) {
        const p = particles[i];
        p.y += p.speedY;
        p.x += Math.sin(p.pulse) * p.speedX;
        p.pulse += p.pulseSpeed;

        if (p.y > height + 10) {
          p.y = -10;
          p.x = Math.random() * width;
        }
        if (p.x > width + 10) p.x = -10;
        if (p.x < -10) p.x = width + 10;

        const currentOpacity = Math.max(0.12, Math.min(0.9, p.opacity + Math.sin(p.pulse) * 0.18));
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);

        if (p.type === 0) {
          // Pure White Ice
          ctx.fillStyle = `rgba(255, 255, 255, ${currentOpacity})`;
          ctx.shadowColor = 'rgba(255, 255, 255, 0.75)';
          ctx.shadowBlur = 5;
        } else if (p.type === 1) {
          // Dark Celestial / Smoky Obsidian Ice
          ctx.fillStyle = `rgba(50, 25, 35, ${currentOpacity * 0.85})`;
          ctx.shadowColor = 'rgba(30, 15, 22, 0.3)';
          ctx.shadowBlur = 3;
        } else {
          // Warm Celestial Gold
          ctx.fillStyle = `rgba(218, 178, 85, ${currentOpacity})`;
          ctx.shadowColor = 'rgba(212, 175, 55, 0.6)';
          ctx.shadowBlur = 4;
        }

        ctx.fill();
      }

      requestAnimationFrame(render);
    }

    requestAnimationFrame(render);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initIceEffect);
  } else {
    initIceEffect();
  }
})();
