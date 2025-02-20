import React, { useState, useRef, useEffect } from 'react';
import { Flag, Timer, Trophy, Users, X, ChevronDown, Search } from 'lucide-react';

function Modal({ isOpen, onClose, children, title }: { isOpen: boolean; onClose: () => void; children: React.ReactNode; title: string }) {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black/80 flex items-center justify-center z-50">
      <div className="bg-[#1E1E1E] rounded-lg p-8 w-full max-w-2xl border-2 border-[#FF1801] relative max-h-[90vh] overflow-y-auto">
        <button 
          onClick={onClose}
          className="absolute top-4 right-4 text-[#B0B0B0] hover:text-white transition-colors"
        >
          <X className="w-6 h-6" />
        </button>
        <h2 className="text-2xl font-bold mb-6 pr-8">{title}</h2>
        {children}
      </div>
    </div>
  );
}

function App() {
  const [isDriverModalOpen, setIsDriverModalOpen] = useState(false);
  const [isConstructorModalOpen, setIsConstructorModalOpen] = useState(false);
  const [isSeasonDropdownOpen, setIsSeasonDropdownOpen] = useState(false);
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedRace, setSelectedRace] = useState<string | null>(null);
  const dropdownRef = useRef<HTMLDivElement>(null);

  const seasons = Array.from({ length: 74 }, (_, i) => 2024 - i);
  const filteredSeasons = seasons.filter(season => 
    season.toString().includes(searchTerm)
  );

  useEffect(() => {
    function handleClickOutside(event: MouseEvent) {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target as Node)) {
        setIsSeasonDropdownOpen(false);
      }
    }

    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  const races = [
    {
      name: 'Bahrain Grand Prix',
      date: '2024-03-02',
      circuit: 'Bahrain International Circuit',
      prediction: 'Verstappen',
      results: [
        { position: 1, driver: 'Max Verstappen', team: 'Red Bull Racing', points: 25, time: '1:31:44.742' },
        { position: 2, driver: 'Sergio Perez', team: 'Red Bull Racing', points: 18, time: '+2.371s' },
        { position: 3, driver: 'Carlos Sainz', team: 'Ferrari', points: 15, time: '+8.645s' },
        { position: 4, driver: 'Charles Leclerc', team: 'Ferrari', points: 12, time: '+11.987s' },
        { position: 5, driver: 'George Russell', team: 'Mercedes', points: 10, time: '+25.232s' },
      ]
    },
    {
      name: 'Saudi Arabian Grand Prix',
      date: '2024-03-09',
      circuit: 'Jeddah Corniche Circuit',
      prediction: 'Perez',
      results: [
        { position: 1, driver: 'Max Verstappen', team: 'Red Bull Racing', points: 25, time: '1:29:23.227' },
        { position: 2, driver: 'Sergio Perez', team: 'Red Bull Racing', points: 18, time: '+13.643s' },
        { position: 3, driver: 'Charles Leclerc', team: 'Ferrari', points: 15, time: '+18.639s' },
        { position: 4, driver: 'Oscar Piastri', team: 'McLaren', points: 12, time: '+32.183s' },
        { position: 5, driver: 'Fernando Alonso', team: 'Aston Martin', points: 10, time: '+35.866s' },
      ]
    },
    {
      name: 'Australian Grand Prix',
      date: '2024-03-24',
      circuit: 'Albert Park Circuit',
      prediction: 'Hamilton',
      results: [
        { position: 1, driver: 'Carlos Sainz', team: 'Ferrari', points: 25, time: '1:30:33.122' },
        { position: 2, driver: 'Charles Leclerc', team: 'Ferrari', points: 18, time: '+2.366s' },
        { position: 3, driver: 'Lando Norris', team: 'McLaren', points: 15, time: '+5.879s' },
        { position: 4, driver: 'Oscar Piastri', team: 'McLaren', points: 12, time: '+8.543s' },
        { position: 5, driver: 'Sergio Perez', team: 'Red Bull Racing', points: 10, time: '+14.166s' },
      ]
    },
    {
      name: 'Japanese Grand Prix',
      date: '2024-04-07',
      circuit: 'Suzuka Circuit',
      prediction: 'Pending',
      results: []
    }
  ];

  const constructorStandings = [
    {
      position: 1,
      team: 'Red Bull Racing',
      points: 87,
      drivers: ['Max Verstappen', 'Sergio Perez']
    },
    {
      position: 2,
      team: 'Ferrari',
      points: 49,
      drivers: ['Charles Leclerc', 'Carlos Sainz']
    },
    {
      position: 3,
      team: 'McLaren',
      points: 28,
      drivers: ['Lando Norris', 'Oscar Piastri']
    },
    {
      position: 4,
      team: 'Mercedes',
      points: 26,
      drivers: ['Lewis Hamilton', 'George Russell']
    },
    {
      position: 5,
      team: 'Aston Martin',
      points: 19,
      drivers: ['Fernando Alonso', 'Lance Stroll']
    },
    {
      position: 6,
      team: 'Alpine',
      points: 12,
      drivers: ['Pierre Gasly', 'Esteban Ocon']
    },
    {
      position: 7,
      team: 'Williams',
      points: 8,
      drivers: ['Alexander Albon', 'Logan Sargeant']
    },
    {
      position: 8,
      team: 'Alfa Romeo',
      points: 6,
      drivers: ['Valtteri Bottas', 'Zhou Guanyu']
    },
    {
      position: 9,
      team: 'Haas F1 Team',
      points: 3,
      drivers: ['Nico Hulkenberg', 'Kevin Magnussen']
    },
    {
      position: 10,
      team: 'AlphaTauri',
      points: 2,
      drivers: ['Yuki Tsunoda', 'Daniel Ricciardo']
    }
  ];

  const driverStandings = [
    { position: 1, name: 'Max Verstappen', points: 51, team: 'Red Bull Racing' },
    { position: 2, name: 'Sergio Perez', points: 36, team: 'Red Bull Racing' },
    { position: 3, name: 'Charles Leclerc', points: 28, team: 'Ferrari' },
    { position: 4, name: 'Carlos Sainz', points: 21, team: 'Ferrari' },
    { position: 5, name: 'Lando Norris', points: 18, team: 'McLaren' },
    { position: 6, name: 'Lewis Hamilton', points: 16, team: 'Mercedes' },
    { position: 7, name: 'Oscar Piastri', points: 10, team: 'McLaren' },
    { position: 8, name: 'George Russell', points: 10, team: 'Mercedes' },
    { position: 9, name: 'Fernando Alonso', points: 9, team: 'Aston Martin' },
    { position: 10, name: 'Lance Stroll', points: 8, team: 'Aston Martin' },
    { position: 11, name: 'Pierre Gasly', points: 6, team: 'Alpine' },
    { position: 12, name: 'Alexander Albon', points: 4, team: 'Williams' },
    { position: 13, name: 'Valtteri Bottas', points: 4, team: 'Alfa Romeo' },
    { position: 14, name: 'Esteban Ocon', points: 4, team: 'Alpine' },
    { position: 15, name: 'Nico Hulkenberg', points: 3, team: 'Haas F1 Team' },
    { position: 16, name: 'Zhou Guanyu', points: 2, team: 'Alfa Romeo' },
    { position: 17, name: 'Yuki Tsunoda', points: 2, team: 'AlphaTauri' },
    { position: 18, name: 'Daniel Ricciardo', points: 0, team: 'AlphaTauri' },
    { position: 19, name: 'Kevin Magnussen', points: 0, team: 'Haas F1 Team' },
    { position: 20, name: 'Logan Sargeant', points: 0, team: 'Williams' }
  ];

  return (
    <div className="min-h-screen bg-[#121212] text-white p-8">
      {/* Header */}
      <header className="flex justify-between items-center mb-8">
        <div className="flex items-center gap-2">
          <Flag className="w-8 h-8 text-[#FF1801]" />
          <h1 className="text-2xl font-bold">F1 PREDICTIONS</h1>
        </div>
        <nav className="flex gap-6 items-center">
          <div className="relative" ref={dropdownRef}>
            <button 
              onClick={() => setIsSeasonDropdownOpen(!isSeasonDropdownOpen)}
              className="flex items-center gap-2 text-[#FFC300] hover:text-white transition-colors"
            >
              SAISON
              <ChevronDown className={`w-4 h-4 transition-transform ${isSeasonDropdownOpen ? 'rotate-180' : ''}`} />
            </button>
            
            {isSeasonDropdownOpen && (
              <div className="absolute top-full mt-2 right-0 w-64 bg-[#1E1E1E] border-2 border-[#FF1801] rounded-lg shadow-xl z-50">
                <div className="p-3 border-b border-[#B0B0B0]/20">
                  <div className="relative">
                    <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-[#B0B0B0]" />
                    <input
                      type="text"
                      placeholder="Rechercher une saison..."
                      value={searchTerm}
                      onChange={(e) => setSearchTerm(e.target.value)}
                      className="w-full bg-[#121212] text-white pl-10 pr-4 py-2 rounded-md focus:outline-none focus:ring-2 focus:ring-[#FF1801]"
                    />
                  </div>
                </div>
                <div className="max-h-64 overflow-y-auto">
                  {filteredSeasons.map((season) => (
                    <button
                      key={season}
                      className="w-full px-4 py-2 text-left hover:bg-[#FF1801] hover:text-white transition-colors"
                      onClick={() => {
                        setIsSeasonDropdownOpen(false);
                        setSearchTerm('');
                      }}
                    >
                      Saison {season}
                    </button>
                  ))}
                </div>
              </div>
            )}
          </div>
          <button className="text-[#B0B0B0] hover:text-white transition-colors">PILOTE</button>
          <button className="text-[#B0B0B0] hover:text-white transition-colors">CONSTRUCTEUR</button>
          <button className="text-[#B0B0B0] hover:text-white transition-colors">CIRCUIT</button>
        </nav>
      </header>

      {/* Standings Section */}
      <div className="grid grid-cols-2 gap-6 mb-8">
        {/* Constructor Standings */}
        <div 
          className="bg-[#1E1E1E] rounded-lg p-6 border-2 border-[#FF1801] cursor-pointer hover:border-[#FFC300] transition-colors"
          onClick={() => setIsConstructorModalOpen(true)}
        >
          <div className="flex items-center gap-2 mb-4">
            <Users className="w-6 h-6 text-[#FF1801]" />
            <h2 className="text-xl font-bold">Classement Constructeurs</h2>
          </div>
          <div className="space-y-4">
            {constructorStandings.slice(0, 3).map((team) => (
              <div key={team.position} className="border-b border-[#B0B0B0]/20 pb-3 last:border-0">
                <div className="flex justify-between items-center mb-2">
                  <div className="flex items-center gap-3">
                    <span className="text-[#FFC300] font-bold">{team.position}</span>
                    <span className="font-medium">{team.team}</span>
                  </div>
                  <span className="text-[#FFC300]">{team.points} pts</span>
                </div>
                <div className="text-sm text-[#B0B0B0] pl-8">
                  {team.drivers.map((driver, index) => (
                    <div key={index}>{driver}</div>
                  ))}
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Driver Standings */}
        <div 
          className="bg-[#1E1E1E] rounded-lg p-6 border-2 border-[#FF1801] cursor-pointer hover:border-[#FFC300] transition-colors"
          onClick={() => setIsDriverModalOpen(true)}
        >
          <div className="flex items-center gap-2 mb-4">
            <Trophy className="w-6 h-6 text-[#FF1801]" />
            <h2 className="text-xl font-bold">Classement Pilotes</h2>
          </div>
          <div className="space-y-3">
            {driverStandings.slice(0, 5).map((driver) => (
              <div key={driver.position} className="flex justify-between items-center border-b border-[#B0B0B0]/20 pb-3 last:border-0">
                <div className="flex items-center gap-3">
                  <span className="text-[#FFC300] font-bold">{driver.position}</span>
                  <span className="font-medium">{driver.name}</span>
                </div>
                <span className="text-[#FFC300]">{driver.points} pts</span>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Races Grid */}
      <div className="grid grid-cols-2 gap-6">
        {races.map((race) => (
          <div 
            key={race.name}
            className="bg-[#1E1E1E] rounded-lg p-6 border-2 border-[#FF1801] hover:border-[#FFC300] transition-colors cursor-pointer"
            onClick={() => setSelectedRace(race.name)}
          >
            <div className="flex justify-between items-center mb-4">
              <h2 className="text-xl font-bold">{race.name}</h2>
              <div className="flex items-center gap-2 text-[#B0B0B0]">
                <Timer className="w-4 h-4" />
                <span>{race.date}</span>
              </div>
            </div>
            
            <div className="grid grid-cols-2 gap-4">
              <div>
                <p className="text-[#B0B0B0] mb-1">Circuit</p>
                <p className="font-medium">{race.circuit}</p>
              </div>
              <div>
                <p className="text-[#B0B0B0] mb-1">Prédiction</p>
                <p className="font-medium text-[#FFC300]">{race.prediction}</p>
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* Race Results Modal */}
      <Modal 
        isOpen={selectedRace !== null} 
        onClose={() => setSelectedRace(null)}
        title={`Résultats - ${selectedRace || ''}`}
      >
        {selectedRace && (
          <div className="space-y-4">
            {races.find(race => race.name === selectedRace)?.results.length === 0 ? (
              <p className="text-center text-[#B0B0B0] py-4">Course à venir</p>
            ) : (
              races.find(race => race.name === selectedRace)?.results.map((result) => (
                <div key={result.position} className="flex items-center justify-between border-b border-[#B0B0B0]/20 pb-4 last:border-0">
                  <div className="flex items-center gap-4">
                    <span className="text-[#FFC300] font-bold w-8">{result.position}</span>
                    <div>
                      <div className="font-medium">{result.driver}</div>
                      <div className="text-sm text-[#B0B0B0]">{result.team}</div>
                    </div>
                  </div>
                  <div className="text-right">
                    <div className="text-[#FFC300] font-bold">{result.points} pts</div>
                    <div className="text-sm text-[#B0B0B0]">{result.time}</div>
                  </div>
                </div>
              ))
            )}
          </div>
        )}
      </Modal>

      {/* Driver Standings Modal */}
      <Modal 
        isOpen={isDriverModalOpen} 
        onClose={() => setIsDriverModalOpen(false)}
        title="Classement Complet des Pilotes"
      >
        <div className="space-y-4">
          {driverStandings.map((driver) => (
            <div key={driver.position} className="flex items-center justify-between border-b border-[#B0B0B0]/20 pb-4 last:border-0">
              <div className="flex items-center gap-4">
                <span className="text-[#FFC300] font-bold w-8">{driver.position}</span>
                <div>
                  <div className="font-medium">{driver.name}</div>
                  <div className="text-sm text-[#B0B0B0]">{driver.team}</div>
                </div>
              </div>
              <span className="text-[#FFC300] font-bold">{driver.points} pts</span>
            </div>
          ))}
        </div>
      </Modal>

      {/* Constructor Standings Modal */}
      <Modal 
        isOpen={isConstructorModalOpen} 
        onClose={() => setIsConstructorModalOpen(false)}
        title="Classement Complet des Constructeurs"
      >
        <div className="space-y-6">
          {constructorStandings.map((team) => (
            <div key={team.position} className="border-b border-[#B0B0B0]/20 pb-6 last:border-0">
              <div className="flex justify-between items-center mb-3">
                <div className="flex items-center gap-4">
                  <span className="text-[#FFC300] font-bold w-8">{team.position}</span>
                  <span className="font-medium text-lg">{team.team}</span>
                </div>
                <span className="text-[#FFC300] font-bold">{team.points} pts</span>
              </div>
              <div className="grid grid-cols-2 gap-2 pl-12 text-[#B0B0B0]">
                {team.drivers.map((driver, index) => (
                  <div key={index}>{driver}</div>
                ))}
              </div>
            </div>
          ))}
        </div>
      </Modal>
    </div>
  );
}

export default App;