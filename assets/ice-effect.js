/**
 * KAVITA — Celestial Ice Crystal Dust Effect
 * Lightweight, high-performance background particle animation.
 * Soft glowing circular ice/crystal particles drifting continuously across the sanctuary.
 */
(function() {
  function initIceEffect() {
    let canvas = document.getElementById('kavitaIceCanvas');
    if (!canvas) {
      canvas = document.createElement('canvas');
      canvas.id = 'kavitaIceCanvas';
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

    const particleCount = window.innerWidth < 768 ? 38 : 68;
    const particles = [];

    for (let i = 0; i < particleCount; i++) {
      particles.push({
        x: Math.random() * width,
        y: Math.random() * height,
        radius: Math.random() * 2.2 + 1.1, // Small circular ice dots (1.1px to 3.3px)
        speedY: Math.random() * 0.42 + 0.2, // Gentle downward drift
        speedX: (Math.random() - 0.5) * 0.28,
        opacity: Math.random() * 0.4 + 0.3,
        pulse: Math.random() * Math.PI * 2,
        pulseSpeed: Math.random() * 0.02 + 0.01,
        isGold: Math.random() < 0.18 // 18% warm celestial gold, 82% glowing ice crystal
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

        if (p.y > height + 8) {
          p.y = -8;
          p.x = Math.random() * width;
        }
        if (p.x > width + 8) p.x = -8;
        if (p.x < -8) p.x = width + 8;

        const currentOpacity = p.opacity + Math.sin(p.pulse) * 0.14;
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);

        if (p.isGold) {
          ctx.fillStyle = `rgba(255, 225, 130, ${Math.max(0.08, currentOpacity)})`;
          ctx.shadowColor = 'rgba(216, 180, 93, 0.45)';
        } else {
          ctx.fillStyle = `rgba(235, 248, 255, ${Math.max(0.08, currentOpacity)})`;
          ctx.shadowColor = 'rgba(180, 225, 255, 0.45)';
        }
        ctx.shadowBlur = 4;
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
