from flask import Flask, render_template_string
import datetime

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BYD AutoShow | Concessionária Oficial BYD</title>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Montserrat', sans-serif;
            background: #0a0a0a;
            color: #ffffff;
            overflow-x: hidden;
        }

        /* Animações */
        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(40px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @keyframes fadeInLeft {
            from { opacity: 0; transform: translateX(-40px); }
            to { opacity: 1; transform: translateX(0); }
        }

        @keyframes fadeInRight {
            from { opacity: 0; transform: translateX(40px); }
            to { opacity: 1; transform: translateX(0); }
        }

        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }

        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }

        /* Header Premium */
        header {
            background: linear-gradient(135deg, #4a148c 0%, #000000 50%, #001a4d 100%);
            color: white;
            padding: 1.5rem 2rem;
            position: relative;
            overflow: hidden;
        }

        .header-content {
            max-width: 1400px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 1rem;
        }

        /* Área da LOGO - logo.png */
        .logo-area {
            display: flex;
            align-items: center;
            gap: 1rem;
            background: rgba(255,255,255,0.1);
            padding: 0.8rem 1.5rem;
            border-radius: 60px;
            backdrop-filter: blur(10px);
            transition: transform 0.3s ease;
        }

        .logo-area:hover {
            transform: scale(1.02);
        }

        /* IMAGEM DA LOGO - logo.png */
        .logo-img {
            width: 60px;
            height: 60px;
            object-fit: contain;
            border-radius: 50%;
        }

        .logo-text {
            font-size: 1.8rem;
            font-weight: 900;
            letter-spacing: 2px;
        }

        .logo-text span {
            color: #7c3aed;
        }

        .logo-tag {
            font-size: 0.8rem;
            opacity: 0.9;
        }

        .header-title {
            text-align: right;
        }

        .header-title h1 {
            font-size: 2.2rem;
            font-weight: 800;
        }

        .header-title h1 span {
            color: #7c3aed;
        }

        .header-title p {
            font-size: 0.9rem;
            opacity: 0.9;
        }

        header::before {
            content: '⚡';
            position: absolute;
            font-size: 300px;
            opacity: 0.05;
            bottom: -80px;
            right: -80px;
            transform: rotate(-15deg);
            animation: float 6s ease-in-out infinite;
        }

        /* Navegação */
        nav {
            background: rgba(0,0,0,0.95);
            backdrop-filter: blur(10px);
            padding: 1rem;
            box-shadow: 0 4px 20px rgba(0,0,0,0.5);
            position: sticky;
            top: 0;
            z-index: 1000;
            text-align: center;
            border-bottom: 1px solid #4a148c;
        }

        nav a {
            color: white;
            text-decoration: none;
            margin: 0 1.5rem;
            font-weight: 600;
            transition: all 0.3s ease;
            position: relative;
            padding: 0.5rem 0;
        }

        nav a::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 50%;
            width: 0;
            height: 3px;
            background: linear-gradient(90deg, #4a148c, #001a4d);
            transition: all 0.3s ease;
            transform: translateX(-50%);
            border-radius: 3px;
        }

        nav a:hover::after {
            width: 100%;
        }

        nav a:hover {
            color: #7c3aed;
        }

        /* Container */
        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 0 2rem;
        }

        /* Banner Hero */
        .hero {
            background: linear-gradient(135deg, #4a148c 0%, #000000 50%, #001a4d 100%);
            border-radius: 40px;
            margin: 2rem 0;
            padding: 4rem;
            text-align: center;
            color: white;
            position: relative;
            overflow: hidden;
            animation: fadeInUp 0.8s ease;
            box-shadow: 0 20px 40px rgba(0,0,0,0.3);
        }

        .hero h2 {
            font-size: 3rem;
            margin-bottom: 1rem;
            font-weight: 900;
        }

        .hero p {
            font-size: 1.2rem;
            margin-bottom: 2rem;
        }

        .hero .btn {
            background: white;
            color: #4a148c;
            border: none;
            padding: 1rem 2.5rem;
            font-size: 1.1rem;
            font-weight: 700;
            border-radius: 50px;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }

        .hero .btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.3);
            background: #7c3aed;
            color: white;
        }

        /* Seção Quem Somos */
        .quem-somos {
            background: rgba(20,20,20,0.95);
            backdrop-filter: blur(10px);
            border-radius: 40px;
            padding: 3rem;
            margin: 2rem 0;
            box-shadow: 0 20px 40px rgba(0,0,0,0.3);
            animation: fadeInLeft 0.8s ease;
            border: 1px solid #4a148c;
        }

        .quem-somos h2 {
            font-size: 2rem;
            color: #7c3aed;
            margin-bottom: 1rem;
            position: relative;
            display: inline-block;
        }

        .quem-somos h2::after {
            content: '';
            position: absolute;
            bottom: -12px;
            left: 0;
            width: 70px;
            height: 4px;
            background: linear-gradient(90deg, #4a148c, #001a4d);
            border-radius: 2px;
        }

        .quem-somos p {
            margin-top: 1.5rem;
            line-height: 1.8;
            color: #cccccc;
        }

        /* Diferenciais */
        .diferenciais {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            margin: 2rem 0;
        }

        .diferencial {
            background: #1a1a1a;
            padding: 2rem;
            border-radius: 25px;
            text-align: center;
            transition: all 0.3s ease;
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            border-top: 4px solid #4a148c;
        }

        .diferencial:hover {
            transform: translateY(-10px);
            box-shadow: 0 20px 40px rgba(74,20,140,0.3);
            border-top-color: #001a4d;
        }

        .diferencial span {
            font-size: 3rem;
            display: block;
            margin-bottom: 1rem;
        }

        .diferencial h3 {
            color: #7c3aed;
        }

        .diferencial p {
            color: #aaaaaa;
        }

        /* Galeria de Carros - 8 CARROS */
        .galeria {
            margin: 4rem 0;
        }

        .galeria h2 {
            font-size: 2.2rem;
            color: #7c3aed;
            margin-bottom: 2.5rem;
            text-align: center;
            position: relative;
        }

        .galeria h2::after {
            content: '';
            position: absolute;
            bottom: -15px;
            left: 50%;
            transform: translateX(-50%);
            width: 80px;
            height: 4px;
            background: linear-gradient(90deg, #4a148c, #001a4d);
            border-radius: 2px;
        }

        .carros-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 2rem;
        }

        .carro {
            background: #1a1a1a;
            border-radius: 25px;
            overflow: hidden;
            box-shadow: 0 15px 35px rgba(0,0,0,0.3);
            transition: all 0.4s ease;
            animation: fadeInUp 0.8s ease;
            border-bottom: 3px solid #4a148c;
        }

        .carro:hover {
            transform: translateY(-15px);
            box-shadow: 0 30px 60px rgba(74,20,140,0.3);
            border-bottom-color: #001a4d;
        }

        .carro-img {
            width: 100%;
            height: 240px;
            object-fit: cover;
            transition: transform 0.5s ease;
        }

        .carro:hover .carro-img {
            transform: scale(1.05);
        }

        .imagem-fallback {
            width: 100%;
            height: 240px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 3rem;
            font-weight: bold;
            color: white;
            transition: transform 0.5s ease;
            background: linear-gradient(135deg, #4a148c, #000000);
        }

        .carro-info {
            padding: 1.5rem;
        }

        .carro h3 {
            font-size: 1.4rem;
            color: #7c3aed;
            margin-bottom: 0.5rem;
        }

        .carro .descricao {
            color: #aaaaaa;
            font-size: 0.85rem;
            line-height: 1.5;
            margin-bottom: 1rem;
        }

        .carro .preco {
            font-size: 1.8rem;
            font-weight: 800;
            color: #ffffff;
            margin: 0.8rem 0;
        }

        .carro .anuncio {
            background: linear-gradient(135deg, #4a148c, #001a4d);
            color: white;
            padding: 0.5rem;
            border-radius: 10px;
            text-align: center;
            font-size: 0.8rem;
            font-weight: 600;
            margin: 0.8rem 0;
        }

        .carro .btn-carro {
            background: linear-gradient(135deg, #4a148c, #000000);
            color: white;
            border: none;
            padding: 0.8rem;
            border-radius: 50px;
            width: 100%;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .carro .btn-carro:hover {
            background: linear-gradient(135deg, #001a4d, #4a148c);
            transform: scale(1.02);
        }

        /* Info */
        .info {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 2rem;
            margin: 3rem 0;
        }

        .info-card {
            background: rgba(20,20,20,0.95);
            backdrop-filter: blur(10px);
            border-radius: 25px;
            padding: 2rem;
            box-shadow: 0 15px 35px rgba(0,0,0,0.2);
            transition: all 0.3s ease;
            border-left: 4px solid #4a148c;
        }

        .info-card:hover {
            transform: translateY(-5px);
            border-left-color: #001a4d;
        }

        .info-card h3 {
            color: #7c3aed;
            margin-bottom: 1rem;
        }

        .info-card i {
            color: #4a148c;
            margin-right: 0.5rem;
        }

        .info-card p {
            color: #cccccc;
        }

        /* Formulário */
        .form-group {
            margin-bottom: 1rem;
        }

        .form-group input,
        .form-group textarea {
            width: 100%;
            padding: 0.8rem;
            border: 2px solid #333;
            border-radius: 12px;
            font-family: 'Montserrat', sans-serif;
            transition: all 0.3s ease;
            background: #2a2a2a;
            color: white;
        }

        .form-group input:focus,
        .form-group textarea:focus {
            outline: none;
            border-color: #4a148c;
        }

        .form-group input::placeholder,
        .form-group textarea::placeholder {
            color: #888;
        }

        .btn-enviar {
            background: linear-gradient(135deg, #4a148c, #001a4d);
            color: white;
            border: none;
            padding: 0.8rem;
            border-radius: 50px;
            width: 100%;
            font-weight: 600;
            cursor: pointer;
        }

        .btn-enviar:hover {
            transform: translateY(-2px);
            background: linear-gradient(135deg, #001a4d, #4a148c);
        }

        /* Footer */
        footer {
            background: linear-gradient(135deg, #4a148c, #000000, #001a4d);
            color: white;
            text-align: center;
            padding: 2rem;
            margin-top: 3rem;
        }

        footer .social a {
            color: white;
            font-size: 1.5rem;
            margin: 0 0.5rem;
            display: inline-block;
            transition: all 0.3s ease;
        }

        footer .social a:hover {
            color: #7c3aed;
            transform: translateY(-3px);
        }

        /* Responsivo */
        @media (max-width: 768px) {
            .header-content {
                flex-direction: column;
                text-align: center;
            }
            .header-title {
                text-align: center;
            }
            nav a {
                margin: 0 0.8rem;
                font-size: 0.8rem;
            }
            .hero h2 {
                font-size: 1.8rem;
            }
            .carros-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="header-content">
            <!-- Área da LOGO - imagem: logo.png -->
            <div class="logo-area">
                <img class="logo-img" src="/static/img/logo.png" alt="Logo BYD" onerror="this.style.display='none'; this.parentElement.querySelector('.logo-text').style.display='flex';">
                <div class="logo-text" style="display: none;">BYD<span>⚡</span></div>
                <div class="logo-tag">Official Store</div>
            </div>
            
            <div class="header-title">
                <h1>BYD <span>AutoShow</span></h1>
                <p>⚡ Build Your Dreams - O futuro da mobilidade elétrica ⚡</p>
            </div>
        </div>
    </header>

    <nav>
        <a href="#home">Home</a>
        <a href="#quem-somos">Quem Somos</a>
        <a href="#galeria">Nossos BYD</a>
        <a href="#contato">Contato</a>
    </nav>

    <div class="container">
        <section id="home" class="hero">
            <h2>⚡ Experimente o futuro ⚡</h2>
            <p>Carros 100% elétricos com tecnologia de ponta, autonomia incrível e design revolucionário</p>
            <button class="btn" onclick="agendarTestDrive()">🚗 Agendar Test Drive</button>
        </section>

        <section id="quem-somos" class="quem-somos">
            <h2>Quem Somos</h2>
            <p>🏭 A <strong>BYD AutoShow</strong> é concessionária oficial da BYD no Brasil, referência em veículos elétricos. Com mais de 10 anos de experiência, oferecemos os melhores modelos com tecnologia inovadora, sustentabilidade e economia para nossos clientes.</p>
            
            <div class="diferenciais">
                <div class="diferencial"><span>🔋</span><h3>100% Elétrico</h3><p>Zero emissões</p></div>
                <div class="diferencial"><span>⚡</span><h3>Carregamento Rápido</h3><p>80% em 30 min</p></div>
                <div class="diferencial"><span>🔧</span><h3>Garantia 8 anos</h3><p>Bateria inclusa</p></div>
                <div class="diferencial"><span>🌍</span><h3>Sustentável</h3><p>Futuro do planeta</p></div>
            </div>
        </section>

        <section id="galeria" class="galeria">
            <h2>⭐ Nossa Frota Premium ⭐</h2>
            <div class="carros-grid">
                <!-- CARRO 1 - DOLPHIN -->
                <div class="carro">
                    <img class="carro-img" src="/static/img/Dolphin.webp" alt="BYD Dolphin" onerror="this.style.display='none'; this.parentElement.querySelector('.imagem-fallback').style.display='flex';">
                    <div class="imagem-fallback" style="display: none;">🐬 BYD DOLPHIN</div>
                    <div class="carro-info">
                        <h3>🐬 BYD DOLPHIN</h3>
                        <p class="descricao">Compacto elétrico perfeito para a cidade. Ágil, econômico e design moderno.</p>
                        <p class="preco">R$ 149.800</p>
                        <div class="anuncio">🎯 Taxa 0% em 24x + Revisão grátis!</div>
                        <button class="btn-carro" onclick="solicitarProposta('BYD Dolphin')">Quero este carro</button>
                    </div>
                </div>
                
                <!-- CARRO 2 - SEAL -->
                <div class="carro">
                    <img class="carro-img" src="/static/img/Seal.webp" alt="BYD Seal" onerror="this.style.display='none'; this.parentElement.querySelector('.imagem-fallback').style.display='flex';">
                    <div class="imagem-fallback" style="display: none;">🏎️ BYD SEAL</div>
                    <div class="carro-info">
                        <h3>🏎️ BYD SEAL</h3>
                        <p class="descricao">Sedan esportivo de alto desempenho. 530cv, 0-100 em 3.8s.</p>
                        <p class="preco">R$ 299.800</p>
                        <div class="anuncio">🎯 Lançamento 2024! Test Drive Grátis</div>
                        <button class="btn-carro" onclick="solicitarProposta('BYD Seal')">Quero este carro</button>
                    </div>
                </div>
                
                <!-- CARRO 3 - YUAN PLUS -->
                <div class="carro">
                    <img class="carro-img" src="/static/img/Yuan.webp" alt="BYD Yuan Plus" onerror="this.style.display='none'; this.parentElement.querySelector('.imagem-fallback').style.display='flex';">
                    <div class="imagem-fallback" style="display: none;">🚙 BYD YUAN PLUS</div>
                    <div class="carro-info">
                        <h3>🚙 BYD YUAN PLUS</h3>
                        <p class="descricao">SUV familiar espaçoso e tecnológico. 420km de autonomia.</p>
                        <p class="preco">R$ 239.800</p>
                        <div class="anuncio">🎯 Isenção de IPVA + Carregador grátis!</div>
                        <button class="btn-carro" onclick="solicitarProposta('BYD Yuan Plus')">Quero este carro</button>
                    </div>
                </div>
                
                <!-- CARRO 4 - HAN -->
                <div class="carro">
                    <img class="carro-img" src="/static/img/Han.webp" alt="BYD Han" onerror="this.style.display='none'; this.parentElement.querySelector('.imagem-fallback').style.display='flex';">
                    <div class="imagem-fallback" style="display: none;">👑 BYD HAN</div>
                    <div class="carro-info">
                        <h3>👑 BYD HAN</h3>
                        <p class="descricao">Sedan premium de luxo. Teto panorâmico, couro legítimo.</p>
                        <p class="preco">R$ 549.800</p>
                        <div class="anuncio">🎯 Entrega Imediata + 8 anos de garantia</div>
                        <button class="btn-carro" onclick="solicitarProposta('BYD Han')">Quero este carro</button>
                    </div>
                </div>
                
                <!-- CARRO 5 - ATTO 3 -->
                <div class="carro">
                    <img class="carro-img" src="/static/img/atto3.webp" alt="BYD Atto 3" onerror="this.style.display='none'; this.parentElement.querySelector('.imagem-fallback').style.display='flex';">
                    <div class="imagem-fallback" style="display: none;">🚗 BYD ATTO 3</div>
                    <div class="carro-info">
                        <h3>🚗 BYD ATTO 3</h3>
                        <p class="descricao">SUV compacto tecnológico. Design moderno e economia.</p>
                        <p class="preco">R$ 219.800</p>
                        <div class="anuncio">🎯 Condições especiais para CNPJ!</div>
                        <button class="btn-carro" onclick="solicitarProposta('BYD Atto 3')">Quero este carro</button>
                    </div>
                </div>
                
                <!-- CARRO 6 - SONG PLUS -->
                <div class="carro">
                    <img class="carro-img" src="/static/img/song.webp" alt="BYD Song Plus" onerror="this.style.display='none'; this.parentElement.querySelector('.imagem-fallback').style.display='flex';">
                    <div class="imagem-fallback" style="display: none;">🚙 BYD SONG PLUS</div>
                    <div class="carro-info">
                        <h3>🚙 BYD SONG PLUS</h3>
                        <p class="descricao">SUV híbrido plug-in. Economia e performance juntos.</p>
                        <p class="preco">R$ 279.800</p>
                        <div class="anuncio">🎯 Primeira revisão grátis!</div>
                        <button class="btn-carro" onclick="solicitarProposta('BYD Song Plus')">Quero este carro</button>
                    </div>
                </div>
                
                <!-- CARRO 7 - E9 -->
                <div class="carro">
                    <img class="carro-img" src="/static/img/e9.webp" alt="BYD e9" onerror="this.style.display='none'; this.parentElement.querySelector('.imagem-fallback').style.display='flex';">
                    <div class="imagem-fallback" style="display: none;">🔋 BYD E9</div>
                    <div class="carro-info">
                        <h3>🔋 BYD E9</h3>
                        <p class="descricao">Sedan executivo elétrico. Luxo e sofisticação.</p>
                        <p class="preco">R$ 399.800</p>
                        <div class="anuncio">🎯 Seguro grátis no primeiro ano!</div>
                        <button class="btn-carro" onclick="solicitarProposta('BYD e9')">Quero este carro</button>
                    </div>
                </div>
                
                <!-- CARRO 8 - TANG -->
                <div class="carro">
                    <img class="carro-img" src="/static/img/tang.webp" alt="BYD Tang" onerror="this.style.display='none'; this.parentElement.querySelector('.imagem-fallback').style.display='flex';">
                    <div class="imagem-fallback" style="display: none;">🚙 BYD TANG</div>
                    <div class="carro-info">
                        <h3>🚙 BYD TANG</h3>
                        <p class="descricao">SUV de 7 lugares. Potência e espaço para toda família.</p>
                        <p class="preco">R$ 459.800</p>
                        <div class="anuncio">🎯 Parcelamento em até 36x!</div>
                        <button class="btn-carro" onclick="solicitarProposta('BYD Tang')">Quero este carro</button>
                    </div>
                </div>
            </div>
        </section>

        <div class="info">
            <div class="info-card">
                <h3><i class="fas fa-map-marker-alt"></i> Localização</h3>
                <p>📍 Av. Engenheiro Luís Carlos Berrini, 1500<br>Brooklin, São Paulo - SP</p>
                <p>🕒 Seg-Sex: 9h às 20h | Sáb: 9h às 16h</p>
                <p>🔌 10 carregadores elétricos gratuitos</p>
            </div>

            <div id="contato" class="info-card">
                <h3><i class="fas fa-envelope"></i> Contato</h3>
                <p><i class="fab fa-whatsapp"></i> (11) 4000-8888</p>
                <p><i class="fas fa-phone"></i> (11) 4000-8889</p>
                <p><i class="fas fa-envelope"></i> vendas@bydautoshow.com.br</p>
                <p><i class="fab fa-instagram"></i> @byd_autoshow</p>
                
                <form onsubmit="event.preventDefault(); enviarMensagem();">
                    <div class="form-group"><input type="text" id="nome" placeholder="Seu nome" required></div>
                    <div class="form-group"><input type="email" id="email" placeholder="Seu e-mail" required></div>
                    <div class="form-group"><textarea id="mensagem" rows="2" placeholder="Mensagem"></textarea></div>
                    <button type="submit" class="btn-enviar">Enviar <i class="fas fa-paper-plane"></i></button>
                </form>
            </div>
        </div>
    </div>

    <footer>
        <div class="social">
            <a href="#"><i class="fab fa-instagram"></i></a>
            <a href="#"><i class="fab fa-facebook"></i></a>
            <a href="#"><i class="fab fa-youtube"></i></a>
            <a href="#"><i class="fab fa-linkedin"></i></a>
        </div>
        <p>BYD AutoShow - Build Your Dreams | {{ ano }}</p>
        <p style="font-size: 0.8rem;">Concessionária oficial BYD - Tecnologia e sustentabilidade</p>
    </footer>

    <script>
        function agendarTestDrive() {
            alert("🚗 Test Drive BYD!\n\n📞 (11) 4000-8888\n💬 WhatsApp: (11) 4000-8888");
        }
        function solicitarProposta(modelo) {
            alert("📞 Proposta " + modelo + "\n\nWhatsApp: (11) 4000-8888");
        }
        function enviarMensagem() {
            let nome = document.getElementById('nome').value;
            if(nome) alert("✅ " + nome + ", mensagem enviada! Entraremos em contato.");
            else alert("⚠️ Digite seu nome.");
        }
    </script>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, ano=datetime.datetime.now().year)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)