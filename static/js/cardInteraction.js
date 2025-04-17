/**
 * Card Interaction Effects
 * Enhances cards with interactive effects and animations throughout the application
 * Versión ligera - efectos sutiles
 */

document.addEventListener('DOMContentLoaded', function() {
    // Detectar si es un dispositivo táctil
    const isTouchDevice = 'ontouchstart' in window || navigator.maxTouchPoints > 0;
    
    // Seleccionar las tarjetas específicas de entradas en ambas vistas
    const entryCards = document.querySelectorAll('.entry-card, .card.form-card, .streak-card, .achievement-card');
    
    console.log(`Card interactions initialized - Found ${entryCards.length} cards - Touch device: ${isTouchDevice}`);
    
    entryCards.forEach(card => {
        // Crear elemento para el efecto de brillo
        const shineEffect = document.createElement('div');
        shineEffect.className = 'shine-effect';
        card.appendChild(shineEffect);
        
        if (!isTouchDevice) {
            // Eventos para dispositivos no táctiles (computadoras)
            
            // Añadir evento para el efecto de brillo al mover el ratón
            // Uso de throttling para limitar las actualizaciones y hacer el efecto más ligero
            let isThrottled = false;
            card.addEventListener('mousemove', function(e) {
                if (!isThrottled) {
                    isThrottled = true;
                    
                    // Calcular posición relativa del cursor
                    const rect = card.getBoundingClientRect();
                    const x = e.clientX - rect.left;
                    const y = e.clientY - rect.top;
                    
                    // Actualizar la posición del efecto de brillo (más sutil)
                    shineEffect.style.background = `radial-gradient(circle at ${x}px ${y}px, rgba(255,255,255,0.2) 0%, rgba(255,255,255,0) 60%)`;
                    
                    // Permitir otra actualización después de 25ms (aprox. 40fps, más que suficiente para este efecto)
                    setTimeout(() => {
                        isThrottled = false;
                    }, 25);
                }
            });
            
            // Eliminar el efecto al salir del elemento
            card.addEventListener('mouseleave', function() {
                shineEffect.style.background = 'none';
            });
            
            // Animación más sutil al entrar con el ratón
            card.addEventListener('mouseenter', function() {
                if (!card.classList.contains('pulse-animation')) {
                    // Añadir clase para la animación de pulso
                    card.classList.add('pulse-animation');
                    
                    // Quitar la clase después de que termine la animación
                    setTimeout(() => {
                        card.classList.remove('pulse-animation');
                    }, 800);
                }
            });
        } else {
            // Eventos para dispositivos táctiles (móviles/tablets)
            // Efectos aún más sutiles en móviles
            
            // Efecto de toque para móviles
            card.addEventListener('touchstart', function(e) {
                // Añadir clase de tarjeta activa al tocar
                card.classList.add('active-card');
                
                // Un efecto de brillo muy sutil en el punto de toque
                if (e.touches && e.touches[0]) {
                    const touch = e.touches[0];
                    const rect = card.getBoundingClientRect();
                    const x = touch.clientX - rect.left;
                    const y = touch.clientY - rect.top;
                    
                    // Brillo más sutil centrado en el punto de toque
                    shineEffect.style.background = `radial-gradient(circle at ${x}px ${y}px, rgba(255,255,255,0.15) 0%, rgba(255,255,255,0) 60%)`;
                }
            });
            
            // Quitar la clase activa después de un tiempo
            card.addEventListener('touchend', function() {
                setTimeout(() => {
                    card.classList.remove('active-card');
                    shineEffect.style.background = 'none';
                }, 300); // Tiempo más corto
            });
        }
    });
    
    // Nota: Los efectos para los badges (insignias) se manejan completamente con CSS
    // para un mejor rendimiento y evitar parpadeos o efectos borrosos
    
    // Efecto para la barra de progreso (funcionará igual en todos los dispositivos)
    const progressBars = document.querySelectorAll('.progress-bar');
    progressBars.forEach(bar => {
        // Obtener el ancho del elemento que debe tener al final
        const targetWidth = bar.style.width || bar.getAttribute('aria-valuenow') + '%';
        
        // Empezar en 0
        bar.style.width = '0%';
        
        // Usar setTimeout para asegurar que la transición se aplique
        setTimeout(() => {
            bar.style.transition = 'width 1.5s ease-out';
            bar.style.width = targetWidth;
        }, 300);
    });
}); 