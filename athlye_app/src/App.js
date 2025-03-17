import React, { useState, useEffect } from 'react';
import { Calendar, MessageSquare, Dumbbell, Salad, ChevronRight, ArrowRight, Menu, X, User } from 'lucide-react';

const AthlyzeApp = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [activeFeature, setActiveFeature] = useState(0);
  const [isVisible, setIsVisible] = useState({});
  const [chatInput, setChatInput] = useState('');
  const [chatMessages, setChatMessages] = useState([
    { sender: 'bot', text: 'Hi there! How can I help with your fitness journey today?' }
  ]);

  const features = [
    {
      id: 'training',
      icon: <Dumbbell className="w-6 h-6 mr-2" />,
      title: 'Personalized Training',
      description: 'AI-powered workout plans based on scientific research, tailored to your specific goals and physiology.',
      color: 'bg-blue-600'
    },
    {
      id: 'nutrition',
      icon: <Salad className="w-6 h-6 mr-2" />,
      title: 'Nutrition Planning',
      description: 'Evidence-based nutrition strategies customized to fuel your performance and support recovery.',
      color: 'bg-green-600'
    },
    {
      id: 'calendar',
      icon: <Calendar className="w-6 h-6 mr-2" />,
      title: 'Smart Calendar',
      description: 'Intelligent scheduling that adapts to your progress, prevents overtraining, and ensures optimal results.',
      color: 'bg-purple-600'
    },
    {
      id: 'assistant',
      icon: <MessageSquare className="w-6 h-6 mr-2" />,
      title: 'AI Coach',
      description: 'Your personal fitness assistant, answering questions with insights backed by scientific research.',
      color: 'bg-orange-600'
    }
  ];

  const handleScroll = () => {
    const sections = document.querySelectorAll('section');
    const scrollPosition = window.scrollY + window.innerHeight * 0.5;

    sections.forEach((section) => {
      const top = section.offsetTop;
      const height = section.offsetHeight;
      
      if (scrollPosition >= top && scrollPosition <= top + height) {
        setIsVisible(prev => ({ ...prev, [section.id]: true }));
      }
    });
  };

  useEffect(() => {
    window.addEventListener('scroll', handleScroll);
    handleScroll();
    
    const featureInterval = setInterval(() => {
      setActiveFeature(prev => (prev + 1) % features.length);
    }, 5000);
    
    return () => {
      window.removeEventListener('scroll', handleScroll);
      clearInterval(featureInterval);
    };
  }, []);

  const sendChatMessage = (e) => {
    e.preventDefault();
    if (!chatInput.trim()) return;
    
    const newMessages = [
      ...chatMessages,
      { sender: 'user', text: chatInput }
    ];
    
    setChatMessages(newMessages);
    setChatInput('');
    
    // Simulate bot response after a short delay
    setTimeout(() => {
      setChatMessages([
        ...newMessages,
        { 
          sender: 'bot', 
          text: 'Based on your profile and our research database, I recommend focusing on compound movements like squats and deadlifts to maximize muscle growth. Would you like me to suggest a specific routine?' 
        }
      ]);
    }, 1000);
  };

  return (
    <div className="min-h-screen bg-gradient-to-b from-gray-900 to-gray-800 text-white">
      {/* Navigation */}
      <nav className="fixed w-full z-50 bg-gray-900/80 backdrop-blur-md">
        <div className="container mx-auto px-4 py-4 flex justify-between items-center">
        <div className="flex items-center space-x-2">
          <svg width="36" height="36" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <defs>
              <linearGradient id="logoGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style={{ stopColor: "#FF6B6B", stopOpacity: 1 }} />
                <stop offset="100%" style={{ stopColor: "#1E90FF", stopOpacity: 1 }} />
              </linearGradient>
            </defs>

            <path 
              d="M50 10 L20 80 L35 80 L50 50 L65 80 L80 80 L50 10 Z"
              fill="none" stroke="url(#logoGradient)" strokeWidth="6" strokeLinejoin="round"
            />
            <circle cx="50" cy="10" r="4" fill="#FF6B6B"/>
            <circle cx="20" cy="80" r="4" fill="#FFD700"/>
            <circle cx="80" cy="80" r="4" fill="#1E90FF"/>
            <circle cx="50" cy="50" r="4" fill="#32CD32"/>
            <path d="M35 80 Q50 100 65 80" stroke="rgba(255, 255, 255, 0.4)" strokeWidth="2" fill="none"/>
          </svg>
          <span className="text-3xl font-bold bg-gradient-to-r from-blue-500 via-purple-500 to-pink-500 text-transparent bg-clip-text">
            Athlyze
          </span>
        </div>
          
          <div className="hidden md:flex space-x-6">
            <a href="#features" className="hover:text-blue-400 transition-colors">Features</a>
            <a href="#how-it-works" className="hover:text-blue-400 transition-colors">How It Works</a>
            <a href="#demo" className="hover:text-blue-400 transition-colors">Demo</a>
            <a href="#testimonials" className="hover:text-blue-400 transition-colors">Testimonials</a>
          </div>
          
          <div className="hidden md:block">
            <button className="bg-blue-600 hover:bg-blue-700 px-6 py-2 rounded-full font-medium transition-colors">
              Get Started
            </button>
          </div>
          
          <button 
            className="md:hidden text-white" 
            onClick={() => setIsMenuOpen(!isMenuOpen)}
          >
            {isMenuOpen ? <X /> : <Menu />}
          </button>
        </div>
        
        {/* Mobile menu */}
        {isMenuOpen && (
          <div className="md:hidden bg-gray-800 p-4">
            <div className="flex flex-col space-y-4">
              <a href="#features" className="hover:text-blue-400" onClick={() => setIsMenuOpen(false)}>Features</a>
              <a href="#how-it-works" className="hover:text-blue-400" onClick={() => setIsMenuOpen(false)}>How It Works</a>
              <a href="#demo" className="hover:text-blue-400" onClick={() => setIsMenuOpen(false)}>Demo</a>
              <a href="#testimonials" className="hover:text-blue-400" onClick={() => setIsMenuOpen(false)}>Testimonials</a>
              <button className="bg-blue-600 hover:bg-blue-700 py-2 rounded-full font-medium transition-colors">
                Get Started
              </button>
            </div>
          </div>
        )}
      </nav>

      {/* Hero Section */}
      <section className="pt-32 pb-20 md:pt-40 md:pb-32 px-4">
        <div className="container mx-auto">
          <div className="flex flex-col lg:flex-row items-center">
            <div className="lg:w-1/2 mb-12 lg:mb-0">
              <h1 className="text-4xl md:text-5xl lg:text-6xl font-bold leading-tight mb-6">
                Transform Your Physique With <span className="text-blue-500">Science</span> and <span className="text-blue-500">AI</span>
              </h1>
              <p className="text-xl text-gray-300 mb-8">
                Athlyze combines cutting-edge AI with scientific research to create personalized training and nutrition plans that deliver real results.
              </p>
              <div className="flex flex-col sm:flex-row gap-4">
                <button className="bg-blue-600 hover:bg-blue-700 px-8 py-3 rounded-full font-medium text-lg transition-colors">
                  Start Your Journey
                </button>
                <button className="border border-blue-500 hover:bg-blue-500/10 px-8 py-3 rounded-full font-medium text-lg transition-colors">
                  Learn More
                </button>
              </div>
            </div>
            <div className="lg:w-1/2 relative">
              <div className="relative z-10 bg-gray-800/80 backdrop-blur-lg rounded-xl p-6 shadow-2xl border border-gray-700">
                <div className="bg-gradient-to-r from-blue-600 to-purple-600 rounded-lg h-1 w-full mb-6"></div>
                <h3 className="text-xl font-semibold mb-4">Your Personalized Plan</h3>
                
                <div className="grid grid-cols-2 gap-4 mb-6">
                  <div className="bg-gray-700/50 p-4 rounded-lg">
                    <p className="text-gray-400 text-sm">Goal</p>
                    <p className="font-medium">Muscle Gain & Strength</p>
                  </div>
                  <div className="bg-gray-700/50 p-4 rounded-lg">
                    <p className="text-gray-400 text-sm">Experience</p>
                    <p className="font-medium">Intermediate</p>
                  </div>
                  <div className="bg-gray-700/50 p-4 rounded-lg">
                    <p className="text-gray-400 text-sm">Days Available</p>
                    <p className="font-medium">4 days/week</p>
                  </div>
                  <div className="bg-gray-700/50 p-4 rounded-lg">
                    <p className="text-gray-400 text-sm">Limitations</p>
                    <p className="font-medium">Knee Injury</p>
                  </div>
                </div>
                
                <div className="flex items-center justify-between mb-3">
                  <div className="flex items-center">
                    <Calendar className="text-blue-500 w-5 h-5 mr-2" />
                    <span className="font-medium">This Week's Plan</span>
                  </div>
                  <span className="text-gray-400 text-sm">Mar 17 - Mar 23</span>
                </div>
                
                <div className="space-y-3 mb-6">
                  <div className="bg-blue-900/30 border border-blue-800 p-3 rounded-lg">
                    <div className="flex justify-between mb-1">
                      <div className="font-medium">Monday: Lower Body Focus</div>
                      <div className="text-blue-400 text-sm">45 min</div>
                    </div>
                    <div className="text-gray-300 text-sm">Squat variations, Romanian deadlifts, leg press</div>
                  </div>
                  <div className="bg-green-900/30 border border-green-800 p-3 rounded-lg">
                    <div className="flex justify-between mb-1">
                      <div className="font-medium">Wednesday: Upper Body Push</div>
                      <div className="text-green-400 text-sm">50 min</div>
                    </div>
                    <div className="text-gray-300 text-sm">Bench press, overhead press, tricep extensions</div>
                  </div>
                </div>
                
                <button className="w-full py-3 bg-blue-600 hover:bg-blue-700 rounded-lg flex items-center justify-center font-medium transition-colors">
                  View Full Plan <ArrowRight className="w-4 h-4 ml-2" />
                </button>
              </div>
              
              <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-full h-full bg-blue-500/20 blur-3xl rounded-full -z-10"></div>
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section id="features" className="py-20 px-4 bg-gray-800/50">
        <div className="container mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold mb-4">Powered by Science and AI</h2>
            <p className="text-xl text-gray-300 max-w-3xl mx-auto">
              Athlyze leverages cutting-edge AI and scientific research to deliver personalized fitness solutions.
            </p>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            {features.map((feature, index) => (
              <div 
                key={feature.id}
                className={`rounded-xl p-6 border border-gray-700 transition-all duration-500 transform ${
                  activeFeature === index ? 'scale-105 shadow-xl shadow-blue-500/10 border-blue-500/50' : 'bg-gray-800/50'
                }`}
              >
                <div className={`${feature.color} p-3 rounded-lg inline-flex items-center justify-center mb-4`}>
                  {feature.icon}
                </div>
                <h3 className="text-xl font-semibold mb-3">{feature.title}</h3>
                <p className="text-gray-300">{feature.description}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* How It Works Section */}
      <section id="how-it-works" className="py-20 px-4">
        <div className="container mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold mb-4">How Athlyze Works</h2>
            <p className="text-xl text-gray-300 max-w-3xl mx-auto">
              Our approach combines your personal data with scientific research for optimal results.
            </p>
          </div>
          
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
            <div className={`bg-gray-800/70 rounded-xl p-6 border border-gray-700 transform transition-all duration-700 ${isVisible['how-it-works'] ? 'translate-y-0 opacity-100' : 'translate-y-12 opacity-0'}`} style={{transitionDelay: '0ms'}}>
              <div className="bg-blue-600 w-12 h-12 rounded-full flex items-center justify-center text-xl font-bold mb-4">1</div>
              <h3 className="text-xl font-semibold mb-3">Create Your Profile</h3>
              <p className="text-gray-300 mb-4">
                Share your demographics, fitness goals, limitations, and preferences to help our AI understand your needs.
              </p>
              <div className="bg-gray-700/50 rounded-lg p-4">
                <div className="flex items-center mb-3">
                  <User className="w-5 h-5 text-blue-400 mr-2" />
                  <span className="font-medium">Profile Metrics</span>
                </div>
                <div className="grid grid-cols-2 gap-3 text-sm">
                  <div>• Age & Gender</div>
                  <div>• Height & Weight</div>
                  <div>• Fitness Level</div>
                  <div>• Medical History</div>
                  <div>• Training History</div>
                  <div>• Diet Preferences</div>
                </div>
              </div>
            </div>
            
            <div className={`bg-gray-800/70 rounded-xl p-6 border border-gray-700 transform transition-all duration-700 ${isVisible['how-it-works'] ? 'translate-y-0 opacity-100' : 'translate-y-12 opacity-0'}`} style={{transitionDelay: '200ms'}}>
              <div className="bg-green-600 w-12 h-12 rounded-full flex items-center justify-center text-xl font-bold mb-4">2</div>
              <h3 className="text-xl font-semibold mb-3">AI Analysis & Recommendation</h3>
              <p className="text-gray-300 mb-4">
                Our AI analyzes your profile and searches our research database to create evidence-based recommendations.
              </p>
              <div className="bg-gray-700/50 rounded-lg p-4">
                <div className="flex items-center mb-3">
                  <Dumbbell className="w-5 h-5 text-green-400 mr-2" />
                  <span className="font-medium">Research Database</span>
                </div>
                <div className="space-y-2 text-sm">
                  <div>• 10,000+ scientific papers</div>
                  <div>• Exercise physiology research</div>
                  <div>• Nutritional science studies</div>
                  <div>• Recovery protocols</div>
                  <div>• Injury prevention methods</div>
                </div>
              </div>
            </div>
            
            <div className={`bg-gray-800/70 rounded-xl p-6 border border-gray-700 transform transition-all duration-700 ${isVisible['how-it-works'] ? 'translate-y-0 opacity-100' : 'translate-y-12 opacity-0'}`} style={{transitionDelay: '400ms'}}>
              <div className="bg-purple-600 w-12 h-12 rounded-full flex items-center justify-center text-xl font-bold mb-4">3</div>
              <h3 className="text-xl font-semibold mb-3">Your Custom Fitness Plan</h3>
              <p className="text-gray-300 mb-4">
                Receive a comprehensive plan including workout schedule, nutrition guide, and ongoing AI coaching.
              </p>
              <div className="bg-gray-700/50 rounded-lg p-4">
                <div className="flex items-center mb-3">
                  <Calendar className="w-5 h-5 text-purple-400 mr-2" />
                  <span className="font-medium">Your Plan Includes</span>
                </div>
                <div className="space-y-2 text-sm">
                  <div>• Weekly workout calendar</div>
                  <div>• Nutrition meal planner</div>
                  <div>• Progress tracking tools</div>
                  <div>• Technique guidance</div>
                  <div>• Adaptive adjustments</div>
                  <div>• 24/7 AI coaching support</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Interactive Demo Section */}
      <section id="demo" className="py-20 px-4 bg-gray-800/50">
        <div className="container mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold mb-4">Experience Athlyze</h2>
            <p className="text-xl text-gray-300 max-w-3xl mx-auto">
              See how our AI coach can answer your fitness questions with science-backed responses.
            </p>
          </div>
          
          <div className={`max-w-3xl mx-auto bg-gray-800 rounded-xl border border-gray-700 overflow-hidden transform transition-all duration-700 ${isVisible['demo'] ? 'translate-y-0 opacity-100' : 'translate-y-12 opacity-0'}`}>
            <div className="bg-gray-900 p-4 border-b border-gray-700 flex items-center">
              <MessageSquare className="text-blue-500 w-5 h-5 mr-2" />
              <h3 className="font-medium">AI Coach Chat</h3>
            </div>
            
            <div className="h-96 p-4 overflow-y-auto flex flex-col space-y-4">
              {chatMessages.map((msg, index) => (
                <div key={index} className={`flex ${msg.sender === 'user' ? 'justify-end' : 'justify-start'}`}>
                  <div 
                    className={`max-w-xs md:max-w-md rounded-lg p-3 ${
                      msg.sender === 'user' 
                        ? 'bg-blue-600 text-white' 
                        : 'bg-gray-700 text-white'
                    }`}
                  >
                    {msg.text}
                  </div>
                </div>
              ))}
            </div>
            
            <div className="p-4 border-t border-gray-700">
              <form onSubmit={sendChatMessage} className="flex">
                <input
                  type="text"
                  value={chatInput}
                  onChange={(e) => setChatInput(e.target.value)}
                  placeholder="Ask about training, nutrition, or recovery..."
                  className="flex-1 bg-gray-700 border border-gray-600 rounded-l-lg px-4 py-2 text-white focus:outline-none focus:border-blue-500"
                />
                <button 
                  type="submit"
                  className="bg-blue-600 hover:bg-blue-700 text-white rounded-r-lg px-4 py-2 flex items-center transition-colors"
                >
                  <ChevronRight className="w-5 h-5" />
                </button>
              </form>
              <div className="mt-2 text-xs text-gray-400">
                Try asking: "What's better for muscle growth, high reps or heavy weights?"
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Testimonials */}
      <section id="testimonials" className="py-20 px-4">
        <div className="container mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold mb-4">Success Stories</h2>
            <p className="text-xl text-gray-300 max-w-3xl mx-auto">
              See how Athlyze has transformed the fitness journeys of our users.
            </p>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {[
              {
                name: "Sarah L.",
                role: "Marathon Runner",
                quote: "Athlyze completely changed my training approach. The personalized nutrition plan helped me shave 15 minutes off my marathon time.",
                image: "/api/placeholder/80/80"
              },
              {
                name: "Mike T.",
                role: "Weightlifter",
                quote: "After years of plateauing, Athlyze analyzed my training and suggested adjustments that helped me add 30lbs to my deadlift in just 2 months.",
                image: "/api/placeholder/80/80"
              },
              {
                name: "Jennifer K.",
                role: "Busy Professional",
                quote: "With limited time to exercise, Athlyze created an efficient program that fits my schedule. The AI coach keeps me accountable and motivated.",
                image: "/api/placeholder/80/80"
              }
            ].map((testimonial, index) => (
              <div 
                key={index}
                className={`bg-gray-800/70 rounded-xl p-6 border border-gray-700 transform transition-all duration-700 ${
                  isVisible['testimonials'] ? 'translate-y-0 opacity-100' : 'translate-y-12 opacity-0'
                }`}
                style={{transitionDelay: `${index * 200}ms`}}
              >
                <div className="flex items-center mb-4">
                  <img 
                    src={testimonial.image} 
                    alt={testimonial.name} 
                    className="w-12 h-12 rounded-full mr-4"
                  />
                  <div>
                    <h4 className="font-medium">{testimonial.name}</h4>
                    <p className="text-gray-400 text-sm">{testimonial.role}</p>
                  </div>
                </div>
                <p className="text-gray-300 italic">"{testimonial.quote}"</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20 px-4 bg-gradient-to-r from-blue-900 to-purple-900">
        <div className="container mx-auto text-center">
          <h2 className="text-3xl md:text-4xl font-bold mb-6">Ready to Transform Your Fitness Journey?</h2>
          <p className="text-xl text-gray-300 max-w-3xl mx-auto mb-8">
            Join thousands of users who are achieving their fitness goals with science-backed, AI-powered plans.
          </p>
          <button className="bg-white text-blue-900 hover:bg-gray-100 px-8 py-3 rounded-full font-medium text-lg transition-colors">
            Start Your Free Trial
          </button>
          <p className="mt-4 text-gray-300">No credit card required. 14-day free trial.</p>
        </div>
      </section>

      <footer className="bg-gray-900 py-12 px-4">
        <div className="container mx-auto">
          <div className="flex flex-col md:flex-row justify-between items-center mb-8">
            <div className="flex items-center mb-6 md:mb-0">
              <Dumbbell className="text-blue-500 w-6 h-6 mr-2" />
              <span className="text-xl font-bold text-white">Athlyze</span>
            </div>
            
            <div className="flex flex-wrap justify-center md:justify-end gap-6 md:space-x-8">
              <a href="#features" className="text-gray-400 hover:text-white transition-colors">Features</a>
              <a href="#how-it-works" className="text-gray-400 hover:text-white transition-colors">How It Works</a>
              <a href="#testimonials" className="text-gray-400 hover:text-white transition-colors">Testimonials</a>
              <a href="#" className="text-gray-400 hover:text-white transition-colors">Privacy</a>
              <a href="#" className="text-gray-400 hover:text-white transition-colors">Terms</a>
            </div>
          </div>
          
          <div className="border-t border-gray-800 pt-8 flex flex-col md:flex-row justify-between items-center">
            <p className="text-gray-500 mb-4 md:mb-0">© 2025 Athlyze. All rights reserved.</p>
            <div className="flex space-x-4">
              <a href="#" className="text-gray-400 hover:text-white transition-colors">
                <svg className="w-6 h-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                  <path fillRule="evenodd" d="M22 12c0-5.523-4.477-10-10-10S2 6.477 2 12c0 4.991 3.657 9.128 8.438 9.878v-6.987h-2.54V12h2.54V9.797c0-2.506 1.492-3.89 3.777-3.89 1.094 0 2.238.195 2.238.195v2.46h-1.26c-1.243 0-1.63.771-1.63 1.562V12h2.773l-.443 2.89h-2.33v6.988C18.343 21.128 22 16.991 22 12z" clipRule="evenodd"></path>
                </svg>
              </a>
              <a href="#" className="text-gray-400 hover:text-white transition-colors">
                <svg className="w-6 h-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                  <path d="M8.29 20.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0022 5.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.072 4.072 0 012.8 9.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84"></path>
                </svg>
              </a>
              <a href="#" className="text-gray-400 hover:text-white transition-colors">
                <svg className="w-6 h-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                  <path fillRule="evenodd" d="M12.315 2c2.43 0 2.784.013 3.808.06 1.064.049 1.791.218 2.427.465a4.902 4.902 0 011.772 1.153 4.902 4.902 0 011.153 1.772c.247.636.416 1.363.465 2.427.048 1.067.06 1.407.06 4.123v.08c0 2.643-.012 2.987-.06 4.043-.049 1.064-.218 1.791-.465 2.427a4.902 4.902 0 01-1.153 1.772 4.902 4.902 0 01-1.772 1.153c-.636.247-1.363.416-2.427.465-1.067.048-1.407.06-4.123.06h-.08c-2.643 0-2.987-.012-4.043-.06-1.064-.049-1.791-.218-2.427-.465a4.902 4.902 0 01-1.772-1.153 4.902 4.902 0 01-1.153-1.772c-.247-.636-.416-1.363-.465-2.427-.047-1.024-.06-1.379-.06-3.808v-.63c0-2.43.013-2.784.06-3.808.049-1.064.218-1.791.465-2.427a4.902 4.902 0 011.153-1.772A4.902 4.902 0 015.45 2.525c.636-.247 1.363-.416 2.427-.465C8.901 2.013 9.256 2 11.685 2h.63zm-.081 1.802h-.468c-2.456 0-2.784.011-3.807.058-.975.045-1.504.207-1.857.344-.467.182-.8.398-1.15.748-.35.35-.566.683-.748 1.15-.137.353-.3.882-.344 1.857-.047 1.023-.058 1.351-.058 3.807v.468c0 2.456.011 2.784.058 3.807.045.975.207 1.504.344 1.857.182.466.399.8.748 1.15.35.35.683.566 1.15.748.353.137.882.3 1.857.344 1.054.048 1.37.058 4.041.058h.08c2.597 0 2.917-.01 3.96-.058.976-.045 1.505-.207 1.858-.344.466-.182.8-.398 1.15-.748.35-.35.566-.683.748-1.15.137-.353.3-.882.344-1.857.048-1.055.058-1.37.058-4.041v-.08c0-2.597-.01-2.917-.058-3.96-.045-.976-.207-1.505-.344-1.858a3.097 3.097 0 00-.748-1.15 3.098 3.098 0 00-1.15-.748c-.353-.137-.882-.3-1.857-.344-1.023-.047-1.351-.058-3.807-.058zM12 6.865a5.135 5.135 0 110 10.27 5.135 5.135 0 010-10.27zm0 1.802a3.333 3.333 0 100 6.666 3.333 3.333 0 000-6.666zm5.338-3.205a1.2 1.2 0 110 2.4 1.2 1.2 0 010-2.4z" clipRule="evenodd"></path>
                </svg>
              </a>
              <a href="#" className="text-gray-400 hover:text-white transition-colors">
                <svg className="w-6 h-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                  <path d="M19.812 5.418c.861.23 1.538.907 1.768 1.768C21.998 8.746 22 12 22 12s0 3.255-.418 4.814a2.504 2.504 0 0 1-1.768 1.768c-1.56.419-7.814.419-7.814.419s-6.255 0-7.814-.419a2.505 2.505 0 0 1-1.768-1.768C2 15.255 2 12 2 12s0-3.255.417-4.814a2.507 2.507 0 0 1 1.768-1.768C5.744 5 11.998 5 11.998 5s6.255 0 7.814.418ZM15.194 12 10 15V9l5.194 3Z" />
                </svg>
              </a>
            </div>
          </div>
          
          <div className="mt-8 text-center">
            <p className="text-gray-500 text-sm">
              Designed with <span className="text-red-500">♥</span> for fitness enthusiasts everywhere
            </p>
          </div>
          
          <div className="mt-6 flex flex-col sm:flex-row justify-center items-center space-y-4 sm:space-y-0 sm:space-x-8">
            <a href="#" className="text-gray-400 hover:text-white transition-colors text-sm flex items-center">
              <svg className="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
              </svg>
              Contact Us
            </a>
            <a href="#" className="text-gray-400 hover:text-white transition-colors text-sm flex items-center">
              <svg className="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
              </svg>
              FAQ
            </a>
            <a href="#" className="text-gray-400 hover:text-white transition-colors text-sm flex items-center">
              <svg className="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"></path>
              </svg>
              Join Our Team
            </a>
          </div>
        </div>
      </footer>
      </div>
  );
}
export default AthlyzeApp;